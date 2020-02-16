from django.urls import path
from . views import home,about,management,production,certificate,infrastructure,network,contact_us

urlpatterns=[
				
		path('',home,name='home'),
		path('about/',about,name='about'),
		path('management/',management,name='management'),
		path('production/',production,name='production'),
		path('certificate/',certificate,name='certificate'),
		path('infrastructure/',infrastructure,name='infrastructure'),
		path('network/',network,name='network'),
		path('contact_us/',contact_us,name='contact_us'),

	]