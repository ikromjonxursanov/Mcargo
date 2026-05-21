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
        ("dispecher", "dispecher"),
        ("yuk tashuvchi firma", "Yuk tashuvchi firma"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='driver')
    phone_number = models.CharField(max_length=13, null=False, blank=False, validators=[phone_validator])
    score = models.FloatField(default=0)
    cenceled_offer = models.BooleanField(default=False)
    learned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.role} - {self.username}"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, null=False, blank=False, validators=[phone_validator])
    score = models.FloatField(default=0)
    cenceled_offer = models.BooleanField(default=False)
    learned = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.full_name

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, null=False, blank=False, validators=[phone_validator])
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')

    summa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    is_initial_borrow = models.BooleanField(default=False)
    is_later_borrow = models.BooleanField(default=False)
    note = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Trucks(models.Model):
    ROLE_CHOICES = [("no", "NO"),
                    ("yes", "Yes"),
                    ]

    uzbek = models.CharField(max_length=200, null=False, blank=False,)
    russian = models.CharField(max_length=200, null=False, blank=False,)
    krilcha = models.CharField(max_length=200, null=False, blank=False,)
    kod = models.CharField(max_length=200, null=False, blank=False,)
    status = models.BooleanField(default=False)
    volume = models.FloatField(default=0)
    volume_inputi = models.FloatField(max_length=20, null=True, blank=True, choices=ROLE_CHOICES, default="yo'/q")
    board_type_inputi= models.FloatField(max_length=20, null=True, blank=True, choices=ROLE_CHOICES, default="yo'/q")
    temperature_inputi= models.FloatField(max_length=20, null=True, blank=True, choices=ROLE_CHOICES, default="yo'/q")
    created_at = models.DateTimeField(auto_now_add=True)
