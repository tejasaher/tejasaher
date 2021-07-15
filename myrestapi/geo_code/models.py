from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 
# Create your models here.
class geo_code(models.Model):



	latitude=models.CharField(max_length=10)
	longitude=models.CharField(max_length=10)
	address=models.CharField(max_length=700)
	seo_id=models.CharField(max_length=300,primary_key=True)

	def	__str__(self):

		return self.seo_id
