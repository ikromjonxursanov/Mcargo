from django.db import models
from django_countries.fields import CountrField

class Ad(models.Model):

    STATUS_CHOICES = [("ad", "Ad"
                      "inporcess", "Inporcess"
                      "delivered", "Delivered")
                      ]

    is_from = models.CountrField()
    is_to = models.CountryField()

    role = models.CharField(max_length=100, choices=STATUS_CHOICES, default="ad")
    load = models.CharField(max_length=100, null=True, Blank=True, default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.is_from}-{self.is_to}"

class Inprocess(models.Model):

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="inprocesses")

    load = models.CharField(max_length=100, null=True, Blank=True, default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.ad}-{self.load}"

class Delivered(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="delivered")



    load = models.CharField(max_length=100, null=True, Blank=True, default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Outprocess(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="outprocesses")


    load = models.CharField(max_length=100, null=True, Blank=True, default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    offer_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ad}-{self.load}"



