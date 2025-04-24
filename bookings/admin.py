from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'slot', 'status', 'booked_at',)
    search_fields = ('user__username', 'experience__title')
    list_filter = ('status',)
    ordering = ('booked_at',)

admin.site.register(Booking, BookingAdmin)