# models.py
from django.db import models
from django.contrib.auth.models import User

class NailArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    nail_artist = models.ForeignKey(NailArtist, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.customer_name} with {self.nail_artist} from {self.start_time} to {self.end_time}"
