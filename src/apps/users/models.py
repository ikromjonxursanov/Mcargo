from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

phone_validator = RegexValidator(regex=r'^\+9989\d{9}$',
                             message='telefon number soralgan fromatda bolsihi kerka ')

class User(AbstractUser):
    ROLE_CHOICES= [
        ('driver', 'Driver'),
        ('manager', 'Manager'),
        ('consignor', 'Consignor'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='driver')
    phone_number = models.CharField(max_length=13, null=False, blank=True, validators=[phone_validator])

    def __str__(self):
        return self.role

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=9, blank=False, null=False, validators=[phone_validator])
    score = models.FloatField(default=0)
    cenceled_offer = models.BooleanField(default=False)
    learned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.full_name

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, null=False, blank=False, validators=[phone_validator])
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name