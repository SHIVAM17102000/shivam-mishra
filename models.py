from django.db import models

# Create your models here.habla
class Contact_us(models.Model):
	name=models.CharField(blank=False,max_length=200)
	email_address=models.EmailField(blank=False,max_length=50)
	phone_number=models.IntegerField()
	your_comment=models.TextField()
