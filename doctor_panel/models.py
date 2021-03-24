from django.db import models
from django import forms

CITY_CHOICES = (
    ("TEHRAN", "tehran"),
    ("MASHHAD", "mashhad"),
)


# Create your models here.
class Doctor(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # token = models.CharField(max_length=300,unique=True)
    name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=30)
    phone_number = models.BigIntegerField()
    medical_association_id = models.IntegerField(unique=True)
    clinic_address = models.TextField()
    city = forms.ChoiceField(choices=CITY_CHOICES)
    medical_expertise = models.TextField()
    degree = models.CharField(max_length=50, default='omomi')
    off_days = models.TextField(null=True)
    opening_time = models.TextField(null=True, default="8:00AM")
    closing_time = models.TextField(null=True, default="12:00PM")


class FreeTimes(models.Model):
    doctor_username = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
