from django.contrib import admin
from django.urls import path
from myweb.view.http_test import http_test
from myweb.view.json_test import json_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('http_test', http_test),
    path('json_test', json_test),
    
]



