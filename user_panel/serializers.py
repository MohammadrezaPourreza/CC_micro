from rest_framework import serializers
from user_panel.models import *
from doctor_panel.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'family_name', 'phone_number', 'email']

class FreeTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeTimes
        fields = ['id','doctor_username','date','time','duration']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'name', 'family_name', 'phone_number', 'medical_association_id','clinic_address','city','medical_expertise','degree','off_days','opening_time','closing_time']

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
