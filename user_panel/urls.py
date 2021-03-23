from django.urls import path
from . import views

app_name = 'user_panel'
urlpatterns = [
    path('add-user/', views.user_list, name='user_list'),
    path('get-doctor-by-city/',views.get_doctor_list_by_city,name='get_doctor_list_by_city'),
    path('get-doctor-freeTimes/',views.get_doctor_freetimes,name='get_doctor_freetimes')
]
