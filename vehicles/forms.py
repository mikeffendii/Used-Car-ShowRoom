from django import forms
from django.forms import ModelForm
from .models import *



class VehicleInquiryForm(ModelForm):
	class Meta:
		model = VehicleInquirie
		fields = '__all__'