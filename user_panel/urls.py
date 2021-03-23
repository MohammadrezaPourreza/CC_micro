from django.urls import path
from . import views

app_name = 'user_panel'
urlpatterns = [
    path('add-user/', views.user_list, name='user_list'),
]
