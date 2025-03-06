from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def index_views(request):
    return HttpResponse("<h1>home page</h1>")


def about_views(request):
    return HttpResponse("<h1>about</h1>")


def contact_views(request):
    return HttpResponse("<h1>contact</h1>")
