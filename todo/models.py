from django.db import models

from datetime import datetime
# Create your models here.
class Todo(models.Model):
    content=models.CharField(max_length=120)
    time_added = models.DateTimeField(default=datetime.now, blank=True)
#next time u r naming a models class-- use capital letter to start d naming intead of small 
