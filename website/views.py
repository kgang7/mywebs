from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def http_test(request):
    return HttpResponse("drood")

def json_test(request):
    return JsonResponse({'abas': 'abaaaaaaaaaaas'})
