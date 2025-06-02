from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import Template



def index_views(request):
    return render(request, 'mysite/index.html')


def about_views(request):
    return render(request, 'mysite/about.html')


def contact_views(request):
    return render(request, 'mysite/contact.html')
