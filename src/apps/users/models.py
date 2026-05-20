from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLLE_CHOICES= [
        ('drivers', 'drivers'),
        ('manager', 'manager'),
        ('consignor', 'consignor'),
    ]
    