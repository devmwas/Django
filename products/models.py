from django.db import models

# Create your models here.
class Product(models.Model):
	"""docstring for Product"""
	title   	= models.TextField()
	description = models.TextField()
	price		= models.TextField()
	summary		= models.TextField(default='This is awesome')
		