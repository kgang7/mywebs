from django.contrib import admin
from django.urls import path
from mywebs.view import http_test
from mywebs.view import json_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('http_test', http_test),
    path('json_test', json_test)
    
]


