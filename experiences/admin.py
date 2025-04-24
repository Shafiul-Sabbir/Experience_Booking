from django.contrib import admin
from .models import Experience, AvailabilitySlot
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'provider', 'start_date', 'end_date', 'capacity')
    search_fields = ('title', 'provider__username')
    list_filter = ('start_date', 'end_date')
    ordering = ('id',)

class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'experience', 'date', 'capacity', 'booked_count')
    search_fields = ('experience__title',)
    list_filter = ('date',)
    ordering = ('date',)

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(AvailabilitySlot, AvailabilitySlotAdmin)