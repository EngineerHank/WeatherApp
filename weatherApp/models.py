from django.db import models

# Create your models here.
class Weather(models.Model):
    location = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=25)
    icon = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location
