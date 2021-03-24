from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from user_panel.models import *
import json
import os
from user_panel.serializers import *
import traceback


# Create your views here.

@csrf_exempt
def user_list(request):
    """
    List all code users, or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse(status=400)


@csrf_exempt
def get_doctor_list_by_city(request):
    if request.method == 'POST':
        city = request.POST['city']
        # acctualy we have to call doctor_panel api
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_data = open(dir_path + '/' + 'doctors.json')
        data1 = json.load(json_data)
        doctors_list = []
        for data in data1:
            if data['city'] == city:
                doctors_list.append(data)
        json_data.close()
        serializer = DoctorSerializer(doctors_list, many=True)
        return JsonResponse(serializer.data, safe=False, status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def get_doctor_freetimes(request):
    if request.method == 'POST':
        doctor = request.POST['doctor_username']
        # acctualy we have to call doctor_panel api
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_data = open(dir_path + '/' + 'freeTimes.json')
        data1 = json.load(json_data)
        freeTimes_list = []
        for data in data1:
            if data['doctor_username'] == doctor:
                freeTimes_list.append(data)
        json_data.close()
        serializer = FreeTimesSerializer(freeTimes_list, many=True)
        return JsonResponse(serializer.data, safe=False, status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def find_doctor_by_name_or_medicalId(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        medical_association_id = request.POST.get('medical_association_id')
        # actually we have to call doctor_panel api
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_data = open(dir_path + '/' + 'doctors.json')
        data1 = json.load(json_data)
        doctors_list = []
        for data in data1:
            if name is not None:
                if data['name'] == name:
                    if data not in doctors_list:
                        doctors_list.append(data)
            if medical_association_id is not None:
                if data['medical_association_id'] == int(medical_association_id):
                    if data not in doctors_list:
                        doctors_list.append(data)
        json_data.close()
        serializer = DoctorSerializer(doctors_list, many=True)
        return JsonResponse(serializer.data, safe=False, status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def edit_user(request):
    # if you wanna edit, you must send all parameters of the user model
    if request.method == 'GET':
        username = request.GET['username']
        user = User.objects.get(username=username)
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        user = User.objects.get(username=data['username'])
        try:
            if data['name']:
                user.name = data['name']
            if data['family_name']:
                user.family_name = data['family_name']
            if data['phone_number']:
                user.phone_number = data['phone_number']
            if data['email']:
                user.email = data['email']
            user.save()
            serializer = UserSerializer(user, many=False)
            return JsonResponse(serializer.data, safe=False)
        except Exception:
            traceback.print_exc()
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)
