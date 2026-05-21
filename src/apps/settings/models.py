from django.db import models
from cities_light.models import Country, Region, City

class Places(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

class Application(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=20, null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# class Adminshare(models.Model):
