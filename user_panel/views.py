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
import datetime


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


@csrf_exempt
def search_doctor_advanced(request):
    if request.method == 'GET':
        city = ''
        medical_expertise = ''
        degree = ''

        try:
            city = request.GET['city']
            medical_expertise = request.GET['medical_expertise']
            degree = request.GET['degree']
        except Exception as e:
            pass

        #     actually we should use doctor service api
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_data = open(dir_path + '/' + 'doctors.json')
        data = json.load(json_data)
        doctors_list = []
        for doc in data:
            if city != '':
                if doc['city'] == city:
                    doctors_list.append(doc)
            else:
                return HttpResponse(status=400)
                break

        for doc in doctors_list:
            if medical_expertise != '':
                if doc['medical_expertise'] != medical_expertise:
                    doctors_list.remove(doc)
            else:
                break

        for doc in doctors_list:
            if degree != '':
                if doc['degree'] != degree:
                    doctors_list.remove(doc)
            else:
                break
        json_data.close()
        serializer = DoctorSerializer(doctors_list, many=True)
        return JsonResponse(serializer.data, safe=False, status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def reserve(request):
    if request.method == 'POST':
        reserve_req = JSONParser().parse(request)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_data = open(dir_path + '/' + 'freeTimes.json')
        data = json.load(json_data)
        for item in data:
            if item['doctor_username'] == reserve_req['doctor_username']:
                if item['date'] == reserve_req['date']:
                    if item['time'] == reserve_req['time']:
                        if item['duration'] == reserve_req['duration']:
                            # bayad az table e free time pak beshe (ke daste ma nist)
                            # bayad be table e reservation ezafe beshe
                            # ama chon table haye doc ro nadarim va foregin key darim nemishe
                            date_time = datetime.datetime.now()
                            doctor = Doctor.objects.get(username=reserve_req['doctor_username'])
                            user = User.objects.get(username=reserve_req['user_username'])
                            reservation = {'doctor_id': doctor.id,
                                           'user_id': user.id,
                                           'reservation_date': reserve_req['date'].replace('/', '-') + ' '
                                                               + reserve_req['time'],
                                           'submit_date': datetime.datetime.strftime(date_time, '%Y-%m-%d %H:%M:%S'),
                                           'is_paid': False}
                            reserve_model = Reservation.objects.create(doctor_id=doctor, user_id=user,
                                                                       reservation_date=reservation['reservation_date'],
                                                                       submit_date=reservation['submit_date'],
                                                                       is_paid=False)
                            reserve_model.save()

                            return JsonResponse(reservation, safe=False, status=201)
            else:
                # TODO mishe bishtar user friendly bashe
                HttpResponse(status=404)
    else:
        return HttpResponse(status=400)

@csrf_exempt
def doctor_comments(request):
    if request.method == 'GET':
        doctor = Doctor.objects.get(username=request.GET['username'])
        comments = Comments.objects.filter(doctor_id=doctor)
        if comments.count() > 1:
            ser = CommentsSerializer(comments, many=True)
            return JsonResponse(ser.data, safe=False, status=201)
        else:
            ser = CommentsSerializer(comments, many=False)
            return JsonResponse(ser.data, safe=False, status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def add_favorite_doctor(request):
    if request.method == 'POST':
        req = JSONParser().parse(request)
        user = User.objects.get(username=req['user_username'])
        doctor = Doctor.objects.get(username=req['doctor_username'])
        date_time = datetime.datetime.now()
        submit_date = datetime.datetime.strftime(date_time, '%Y-%m-%d')
        fav_doc = FavoriteDoctor.objects.create(user_id=user, doctor_id=doctor, add_date=submit_date)
        fav_doc.save()
        response = {
            'user': req['user_username'],
            ' doctor': req['doctor_username'],
            'adding_date': submit_date
        }
        return JsonResponse(response, status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def favorite_doctors(request):
    if request.method == 'GET':
        user = User.objects.get(username=request.GET['username'])
        favorite_docs = FavoriteDoctor.objects.filter(user_id=user)
        if favorite_docs.count() > 1:
            ser = FavoriteDoctorSerializer(favorite_docs, many=True)
            return JsonResponse(ser.data, status=201, safe=False)
        elif favorite_docs == 1:
            ser = FavoriteDoctorSerializer(favorite_docs, many=False, safe=False)
            return JsonResponse(ser.data, status=201)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=400)
