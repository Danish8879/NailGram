# urls.py
from django.urls import path
from .views import book_appointment

urlpatterns = [
    # path('calendar/', calendar_view, name='calendar'),
    # path('api/appointments/', get_appointments, name='get_appointments'),
    # path('book/', book_appointment, name='book_appointment'),
    path('book_appointment/', book_appointment, name='book_appointment'),
    
]
