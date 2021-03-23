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


# Create your views here.

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
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
def get_doctor_list_by_city(request):
    if request.method == 'POST':
        city = request.POST['city']
        #acctualy we have to call doctor_panel api
        dir_path = os.path.dirname(os.path.realpath(__file__))
        json_data = open(dir_path + '/' + 'doctors.json')
        data1 = json.load(json_data)
        doctors_list = []
        for data in data1:
            if data['city'] == city:
                doctors_list.append(data)
        json_data.close()
        json_string = json.dumps(doctors_list)
        return HttpResponse(json_string,status=201)
    else:
        return HttpResponse(status=400)