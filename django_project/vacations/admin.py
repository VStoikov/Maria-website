from django.contrib import admin

# Register your models here.

from .models import Vacations

class VacationsAdmin(admin.ModelAdmin):
	list_display = ["date_start","date_end","reason"]
	list_filter = ('date_start','update_date')

admin.site.register(Vacations, VacationsAdmin)