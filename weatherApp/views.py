from django.shortcuts import render
import requests
from .models import Weather
from django.conf import settings

# Create your views here.

def home(request):
    Weather_data = None

    if request.method == 'POST':
        location = request.POST['location']
        api_key = settings.WEATHER_API_KEY
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')
        
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']

            weather_data = Weather.objects.create(location=location, 
                                                  temperature=temperature, 
                                                  humidity=humidity,
                                                    description=description,
                                                      icon=icon)
            weather_data.save()

            weather = Weather.objects.all()

            return render(request, 'weatherApp/home.html', {'weather': weather})