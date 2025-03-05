from projectApp.view import http_test
from projectApp.view import json_test

urlpatterns = [
    path('http_test', http_test),
    path('json_test', json_test),
    
]