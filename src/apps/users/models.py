from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLLE_CHOICES= [
        ('drivers', 'drivers'),
        ('manager', 'manager'),
        ('consignor', 'consignor'),
    ]


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    score = models.FloatField(default=0)
    cenceled_offer = models.BooleanField(default=False)
    learned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)