from django.contrib import admin
from django.urls import path

from simplecalculator import views

urlpatterns = [
    
    path('', views.compute),
    path('<path:input_str>', views.compute),
]
