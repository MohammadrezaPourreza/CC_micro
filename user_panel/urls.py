from django.urls import path
from . import views

app_name = 'user_panel'
urlpatterns = [
    path('add-user/', views.user_list, name='user_list'),
    path('add-comment/', views.add_comment, name='add_comment'),
    path('get-doctor-by-city/', views.get_doctor_list_by_city, name='get_doctor_list_by_city'),
    path('get-doctor-freeTimes/', views.get_doctor_freetimes, name='get_doctor_freetimes'),
    path('find-doctor-by-name-or-medicalId/', views.find_doctor_by_name_or_medicalId,
         name='find_doctor_by_name_or_medicalId'),
    path('edit-user/', views.edit_user, name='edit_user'),
    path('search-doctor-advanced/', views.search_doctor_advanced, name='search_doctor_advanced'),
    path('reserve/', views.reserve, name='reserve'),
    path('doctor-comments/', views.doctor_comments, name='doctor_comments'),
    path('add-favorite-doctor/', views.add_favorite_doctor, name='add_favorite_doctor'),
    path('favorite-doctors/', views.favorite_doctors, name='favorite_doctors')
]
