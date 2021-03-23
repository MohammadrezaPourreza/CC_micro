from rest_framework import serializers
from user_panel.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'family_name', 'phone_number', 'email']


class FavoriteDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteDoctor
        fields = ['id', 'add_date', 'doctor_id', 'user_id']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user_id', 'doctor_id', 'comment', 'comment_date']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'user_id', 'doctor_id', 'submit_date', 'reservation_date', 'is_paid']
