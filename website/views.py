from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import Template



def index_views(request):
    return render(request, 'websites/index.html')


def about_views(request):
    return render(request, 'websites/about.html')


def contact_views(request):
    return render(request, 'websites/contact.html')
