import django_filters 
from .models import *
from django import forms
from django_filters import CharFilter

class VehicleFilter(django_filters.FilterSet):

	name = CharFilter(field_name='name',lookup_expr='icontains',label='Make')
	class Meta:
		model = Vehicle
		fields = '__all__'
		exclude = ['short_description','long_description','image','listed_at']