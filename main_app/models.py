from django.db import models
from django.urls import reverse
# Create your models here.

OIL_CHANGE = (
    ('5.000', 'miles'),
    ('10.000', 'miles'),
    ('15.000', 'miles'),
    ('20.000', 'miles'),
    ('25.000', 'miles'),
    ('30.000', 'miles'),
    ('35.000', 'miles'),
    ('40.000', 'miles'),
    ('45.000', 'miles'),
    ('50.000', 'miles'),
    ('55.000', 'miles'),
    ('60.000', 'miles'),
)

class Car(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)  
    color = models.CharField(max_length=15)  
    vin = models.CharField(max_length=17) 
    year = models.IntegerField()
    
    def __str__(self):
        return self.make 

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'car_id': self.id })

class Maintenance(models.Model):
    date = models.DateField()
    oil = models.CharField(
        max_length=7,
        choices=OIL_CHANGE,
        default=OIL_CHANGE[0][0]
        )
    tire_rotation = models.CharField(max_length=15)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_oil_display()} on {self.date}'
