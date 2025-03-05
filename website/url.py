from django.contrib import admin
from django.urls import path 
from website.views import http_test
from website.views import json_test

urlpatterns = [
    path('http_test', http_test),
    path('json_test', json_test),
    
]
