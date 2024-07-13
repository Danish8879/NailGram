from django.db import models
import uuid
# Create your models here.

class services(models.Model):
    service_id = models.UUIDField(primary_key=True)
    service_name = models.CharField(max_length=100,unique=True)
    service_description = models.CharField(max_length=200,null=True,blank=True)
    service_cost = models.FloatField(default=0)
    service_duration_hrs=models.FloatField()

