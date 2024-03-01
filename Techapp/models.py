from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='example@gmail.com')
    mobile = models.BigIntegerField(default='123456789')

    def __str__(self):
        return self.user.username


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.IntegerField()  # Assuming you're storing the rating as an integer
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)


class Booking(models.Model):
    SERVICE_CHOICES = [
        ('laptop-repair', 'Laptop Repair'),
        ('mobile-repair', 'Mobile Device Repair'),
        ('tablet-repair', 'Tablet Repair'),
        ('desktop-repair', 'Desktop Repair'),
        ('software-install', 'Software Installation'),
        ('upgrades-maintenance', 'Upgrades & Maintenance'),
    ]

    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # You can adjust the max length as needed
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
