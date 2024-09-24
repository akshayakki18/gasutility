from django.db import models
from django.utils import timezone


# Create your models here.
class servicelist(models.Model):
    address = models.TextField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.email


class serviceform(models.Model):
    SERVICE_REQUEST_TYPES = [
        ('Installation', 'Installation'),
        ('Repair', 'Repair'),
        ('Maintenance', 'Maintenance'),
        ('Express Shipping', 'Express Shipping'),
        ('Extended Warranty', 'Extended Warranty')
    ]

    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(max_length=800, blank=False)
    service_request_type = models.CharField(max_length=100, choices=SERVICE_REQUEST_TYPES, blank=False)
    submission_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, default='Pending')
    resolution_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
