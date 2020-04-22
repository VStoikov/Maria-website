from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
	class Meta:
		model=Appointment
		fields=[
		    "date",
		    "time_start",
		    "time_end",
		    "service",
		    "appointment_with"
		]