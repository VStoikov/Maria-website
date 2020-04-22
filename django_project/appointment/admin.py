from django.contrib import admin

# Register your models here.

from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
	list_display = ["date", "time_start","time_end","service","appointment_with"]
	list_filter = ('date', 'update_time')

admin.site.register(Appointment, AppointmentAdmin)