from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(default='', max_length=30)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	description = models.TextField(default='', max_length=500)
	twitter = models.URLField(default='https://www.twitter.com')
	instagram = models.URLField(default='https://www.instagram.com')
	facebook = models.URLField(default='https://www.facebook.com')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kawrgs):
		super().save(*args, **kawrgs)

		img = Image.open(self.image.path)

		#if img.height > 300 or img.width > 300:
		#	output_size = (300, 300)
		#	img.thumbnail(output_size)
		#	img.save(self.image.path)