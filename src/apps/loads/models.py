from django.db import models
from django_countries.fields import CountryField
from apps.users.models import Driver

class Ad(models.Model):

    STATUS_CHOICES = [("ad", "Ad"),
                      ("inprocess", "Inprocess"),
                      ("delivered", "Delivered"),
                       ("unapplied", "Unapplied")
                      ]

    from_country = CountryField()
    to_country = CountryField()

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="ad")
    load = models.CharField(max_length=100, null=True, blank=True, default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    offer_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.from_country}-{self.to_country}"

class Driverlocation(models.Model):
    STATUS_CHOICES = [("all", "All"),
                      ("empty", "Empty"),
                      ("on_road", "On_road")
                      ]


    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name="driverlocation")

    longitude = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    latitude = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    note = models.TextField(max_length=1000, null=True, Blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
