from django.db import models
from django_countries.fields import CountryField

class Ad(models.Model):

    STATUS_CHOICES = [("ad", "Ad"),
                      ("inporcess", "Inporcess"),
                      ("delivered", "Delivered")
                      ]

    is_from = models.CountryField()
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

class Driverlocation(models.Model):
    STATUS_CHOICES = [("all", "All"),
                      ("empty", "Empty"),
                      ("on_road", "On_road")
                      ]


    driver = models.OneToOneFiled(Driver, on_delete=models.CASCADE, related_name="driverlocation")

    lontitude = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    lattitude = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    note = models.TextField(max_length=1000, null=True, Blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
