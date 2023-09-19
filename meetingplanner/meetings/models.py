from django.db import models
from datetime import time

# Create your models here.

class Meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey('Rooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
    
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    floor_no = models.IntegerField()
    room_no = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_no} on floor {self.floor_no}"
