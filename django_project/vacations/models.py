from django.db import models
from django.contrib.auth.models import User

class Vacations(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	date_start=models.CharField(max_length=50)
	date_end=models.CharField(max_length=50)
	reason=models.CharField(max_length=150)
	update_date=models.DateField(auto_now=True, auto_now_add=False)
	frist_date=models.DateField(auto_now=False, auto_now_add=True)
    
    #show filed in admin panel
	def __str__(self):
		return self.date
	def __str__(self): 
		return self.date_start
	def __str__(self): 
		return self.date_end
	def __str__(self): 
		return self.reason