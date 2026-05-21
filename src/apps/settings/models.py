from django.db import models
from cities.models import Country, Region, City

class Places(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

# class Application(models.Model):
#     full_name = models.CharField(max_length=100, null=False, blank=False)
#     