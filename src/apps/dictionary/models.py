from django.db import models

class Reference(models.Model):
    TYPE_CHOICES = [
        ("currency", "Currency"),
        ("document", "Document"),
        ("body", "Body"),
        ("unit", "Unit"),
        ("carrier", "Carrier"),
        ("cargo_status", "Cargo Status"),
        ("offer_status", "Offer Status"),
        ("payment", "Payment"),
        ("partial_load", "Partial Load"),
        ("user_type", "User Type"),
        ("truck_type", "Truck Type"),
    ]

    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="currency")

    name_uz = models.CharField(max_length=120)
    name_ru = models.CharField(max_length=120)
    name_curl = models.CharField(max_length=120)

    code = models.CharField(max_length=120, null=True, blank=True)
    symbol = models.CharField(max_length=120, null=True, blank=True)
    is_active = models.BooleanField(max_length=20, choices=STATUS_CHOICES, default="active")