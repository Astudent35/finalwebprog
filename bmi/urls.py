from django.urls import path
from . import views

urlpatterns = [
    path('bmi/', views.bmi, name='bmi'),
    path('yourbmi/', views.yourbmi, name='yourbmi'),
]
