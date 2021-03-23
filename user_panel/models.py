from django.db import models
import doctor_panel.models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    # token = models.CharField(max_length=300,unique=True)
    name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=30)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=254, null=True)


class FavoriteDoctor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor_panel.models.Doctor, on_delete=models.CASCADE)
    add_date = models.DateField()


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor_panel.models.Doctor, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField()


class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(doctor_panel.models.Doctor, on_delete=models.CASCADE)
    submit_date = models.DateTimeField()
    reservation_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
