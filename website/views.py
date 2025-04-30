from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import Template



def index_views(request):
    return render(request, 'templates/mysite/index.html')


def about_views(request):
    return render(request, 'templates/about.html')


def contact_views(request):
    return render(request, 'templates/contact.html')
