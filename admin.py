from django.contrib import admin
from .models import Contact_us
class Contact(admin.ModelAdmin):
	list_display=['name']
admin.site.register(Contact_us,Contact)

# Register your models here.
