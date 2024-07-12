# models.py
from django.db import models
from django.contrib.auth.models import User

import datetime

import uuid



class Appointment(models.Model):
    
    appointment_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    #customer_name = models.CharField(max_length=100)
    appointment_date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.customer_name} on {self.appointment_date} from {self.start_time} to {self.end_time}"
