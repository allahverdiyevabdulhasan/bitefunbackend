from django.db import models
from user_management.models import User
from core.models import BaseModel

class Venue(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='venues')
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    menu = models.JSONField()  # Restoran menüsü olarak JSON formatında

    def __str__(self):
        return self.name

class Event(BaseModel):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    attendees = models.ManyToManyField(User, related_name='events')

    def __str__(self):
        return self.name
