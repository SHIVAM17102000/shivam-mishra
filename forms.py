from django import forms
from .models import Contact_us



class ContactForm(forms.ModelForm):
	class Meta:
		model=Contact_us
		fields=[
		'name',
		'email_address',
		'phone_number',
		'your_comment' ,


		]