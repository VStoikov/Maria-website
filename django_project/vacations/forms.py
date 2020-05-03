from django import forms
from .models import Vacations

class VacationsForm(forms.ModelForm):
	class Meta:
		model=Vacations
		fields=[
		    "date_start",
		    "date_end",
		    "reason"
		]