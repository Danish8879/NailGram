from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    #return HttpResponse("Home page reached")
    return render(request, 'home/index.html')

