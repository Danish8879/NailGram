from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_services(request):
    return HttpResponse("Service Page reached")