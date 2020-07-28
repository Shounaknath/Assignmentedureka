from django.db import models

# Create your models here.
class Contact(models.Model):
	email = models.EmailField(max_length=50)
	phone= models.CharField(max_length=20, default='')
	desc= models.CharField(max_length=1000)
	date= models.DateField(auto_now_add=False)

	def __str__(self):
		return self.email
