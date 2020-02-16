from django.shortcuts import render
from .models import Contact_us
from . forms import ContactForm

# Create your views here.
def home(request):
	return render(request,'home.html',{})
def about(request):
	return render(request,'about.html',{})
def management(request):
	return render(request,'management.html',{})
def production(request):
	return render(request,'production.html',{})
def network(request):
	return render(request,'network.html',{})
def certificate(request):
	return render(request,'certificate.html',{})
def infrastructure(request):
	return render(request,'infrastructure.html',{})
def contact_us(request):
	form=ContactForm(request.POST or None)
	# if form.is_valid():
	# 	name=form.cleaned_data.get('name')
	# 	email_address=form.cleaned_data.get('email_address')
	# 	phone_number=form.cleaned_data.get('phone_number')
	# 	your_comment=form.cleaned_data.get('your_comment')

	# 	instance=ContactForm()
	# 	instance.name=name
	# 	instance.email_address=email_address
	# 	instance.phone_number=phone_number
	# 	instance.your_comment=your_comment

	# 	instance.save()
	# 	form=ContactForm()
	# context={

	# 			'form':form
	# }
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		
		form=ContactForm()
	context={
				'form':form
	}
	

	return render(request,'contact.html',context)