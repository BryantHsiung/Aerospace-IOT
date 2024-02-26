from django.urls import path
from . import views

urlpatterns = [
    path('temperature/', views.temperature, name = "temperature"),
    path('temperature_analysis', views.temperature_analysis, name = "temperature_analysis"),
]