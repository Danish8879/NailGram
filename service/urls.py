from django.urls import path
from service.views import get_services

urlpatterns = [
    path('',get_services,name="get_services"),
]
