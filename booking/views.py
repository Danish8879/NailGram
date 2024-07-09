# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse

#from .forms import AppointmentForm



from django.http import JsonResponse
from django.views.decorators.http import require_GET
#from .models import Appointment
from datetime import datetime

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




@require_GET
def check_availability(request):
    print("check availabiltity function reached ......")
    date = request.GET.get('date')

    print("date = ",date)
    
    #Example logic to check availability
    times = ['01:00 PM', '03:00 PM', '05:00 PM', '07:00 PM', '09:00 PM', '11:00 PM']
    availability_data = {
        '01:00 PM': 'available',
        '03:00 PM': 'unavailable',
        '05:00 PM': 'available',
        '07:00 PM': 'available',
        '09:00 PM': 'unavailable',
        '11:00 PM': 'available',
        }

    # for time in times:
    #     time_slot = datetime.combine(date.date(), datetime.strptime(time, '%I:%M %p').time())
    #     is_available = not Appointment.objects.filter(appointment_time=time_slot).exists()
    #     availability_data[time] = 'available' if is_available else 'unavailable'

    return JsonResponse(availability_data)
