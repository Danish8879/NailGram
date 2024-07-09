# models.py
from django.db import models
from django.contrib.auth.models import User

import uuid

# class NailArtist(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Appointment(models.Model):
    
#     appointment_id = models.UUIDField(primary_key=True)
#     customer_name = models.ForeignKey(User.username)
#     #nail_artist = models.ForeignKey(NailArtist, on_delete=models.CASCADE)
#     #customer_name = models.CharField(max_length=100)
#     appointment_date = models.DateField()
#     start_time = models.TimeField()
#     #end_time = models.DateTimeField()

#     def __str__(self):
#         return f"{self.customer_name} on {self.appointment_date} from {self.start_time} to {self.end_time}"
