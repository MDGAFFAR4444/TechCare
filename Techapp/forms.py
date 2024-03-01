# booking/forms.py

from django import forms


class BookingForm(forms.Form):
    SERVICE_CHOICES = [
        ('laptop-repair', 'Laptop Repair'),
        ('mobile-repair', 'Mobile Device Repair'),
        ('tablet-repair', 'Tablet Repair'),
        ('desktop-repair', 'Desktop Repair'),
        ('software-install', 'Software Installation'),
        ('upgrades-maintenance', 'Upgrades & Maintenance'),
    ]

    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=True
    )
