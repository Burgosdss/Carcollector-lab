from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.


class Addon(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('addons_detail', kwargs={ 'addon_id': self.id })

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
    addons = models.ManyToManyField(Addon)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.make 

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'car_id': self.id })
    
    # Recalculate at 6 month 
    # def maintenance_for_year(self):
    #   return self.maintenance_set.filter(date=date.today()).count() >= len(OIL_CHANGE)

class Maintenance(models.Model):
    date = models.DateField('maintenance date')
    oil = models.CharField(
        max_length=7,
        choices=OIL_CHANGE,
        default=OIL_CHANGE[0][0]
        )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_oil_display()} on {self.date}'

class Photo(models.Model):
  url = models.CharField(max_length=200)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for car_id: {self.car_id} @{self.url}"