from django.http import HttpResponse
from django.json import JsonResponse



def http_test(request):
    return HttpResponse("drood")

def json_test(request):
    return JsonResponse("abas")

