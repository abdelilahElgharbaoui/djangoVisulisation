# qcm/urls.py
from django.urls import path
from .views import display_questions
from django.contrib import admin

urlpatterns = [
    path('questions/', display_questions, name='questions'),
]
