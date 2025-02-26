from django.contrib import admin
from django.urls import path
from myweb.view import http_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('http_test', http_test)
    
]


