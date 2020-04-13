from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

SERVICE_CHOICES = (
	('service', 'Услуга'),
	('haircut', 'Прическа'),
)

SERVICE_TYPE = (
	('spray', 'Боадисване'),
	('dryer', 'Сешуар'),
	('barber', 'Подстригване'),
	('location', 'Услуга на адрес'),
	('razor', 'Бръснар'),
)

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete = delete post on user delete

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Page(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.title

class Services(models.Model):
	title = models.CharField(max_length=100)
	service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='service')
	description = models.TextField(blank=True, null=True)
	price = models.FloatField(default=0)
	service_icon = models.CharField(max_length=20, choices=SERVICE_TYPE, default='barber')
	image = models.ImageField(default='default_service.jpg', upload_to='service_pics')

	def __str__(self):
		return self.title

	def save(self, *args, **kawrgs):
		super().save(*args, **kawrgs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)