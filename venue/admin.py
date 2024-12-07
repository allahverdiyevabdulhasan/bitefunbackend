from django.contrib import admin
from .models import Venue, Event
from user_management.models import User  # Eğer kullanıcıyı admin'de kullanmak istiyorsanız, bu satırı ekleyin.

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'owner', 'latitude', 'longitude')
    search_fields = ('name', 'address', 'owner__username')
    list_filter = ('owner',)  # Sahiplerine göre filtreleme
    ordering = ('name',)  # Adına göre sıralama

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'date', 'get_attendees_count')
    search_fields = ('name', 'description', 'venue__name')
    list_filter = ('date', 'venue')  # Etkinlik tarihine ve mekanına göre filtreleme
    ordering = ('date',)  # Tarihe göre sıralama

    # Attendees sayısını kolayca görmek için özel bir metod
    def get_attendees_count(self, obj):
        return obj.attendees.count()
    get_attendees_count.short_description = 'Attendees Count'  # Kolon adı

