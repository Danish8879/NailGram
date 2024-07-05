# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import NailArtist, Appointment
from .forms import AppointmentForm

# def calendar_view(request):
#     nail_artists = NailArtist.objects.all()
#     return render(request, 'booking/calendar.html', {'nail_artists': nail_artists})

# def get_appointments(request):
#     appointments = Appointment.objects.all()
#     events = []
#     for appointment in appointments:
#         events.append({
#             'title': f"{appointment.customer_name} with {appointment.nail_artist.name}",
#             'start': appointment.start_time.isoformat(),
#             'end': appointment.end_time.isoformat(),
#         })
#     return JsonResponse(events, safe=False)

def book_appointment(request):
    print("booking function readched.......")
    return render(request, 'booking/booking.html')
