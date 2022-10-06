from django.urls import path

from . import views

urlpatterns = [
    path('', views.seleccion, name='seleccion'),
    path('user-settings/',views.user_data,name="user_data"),
]