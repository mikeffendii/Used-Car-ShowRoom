from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.core.paginator import Paginator
from django.core import serializers
from .forms import *
from .filters import VehicleFilter
import json
from django.views.generic import ListView

# class VehicleListView(ListView):
# 	model = Vehicle
# 	template_name = 'vehicles/UsedCars.html'

# 	def get_context_data(self,**kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context["qs_json"] = json.dumps(list(Vehicle.objects.values()),default=str)
# 		return context

# Create your views here.
def homePage(request):
	vehicles = Vehicle.objects.all().order_by('-id')

	context = {
		'vehicles': vehicles,
	}
	return render(request, 'vehicles/Homepage.html',context)



def usedCarsPage(request):
	if 'q' in request.GET:
		q=request.GET['q']
		vehicles = Vehicle.objects.filter(name__icontains=q).order_by('-id')
	else:
		vehicles = Vehicle.objects.all().order_by('-id')
		
	
	vehicle_filter = VehicleFilter(request.GET,queryset=vehicles)
	vehicles = vehicle_filter.qs

	paginator = Paginator(vehicles,4)
	page_num = request.GET.get('page',1)
	vehicles = paginator.page(page_num)



	context = {
		'vehicles': vehicles,
		'vehicle_filter': vehicle_filter,
		'qs_json' : json.dumps(list(Vehicle.objects.values()),default=str)
	}
	return render(request, 'vehicles/UsedCars.html', context)

def usedCarDetailPage(request,veh_id):
	veh = Vehicle.objects.get(id=veh_id)
	if  request.headers.get('x-requested-with') == 'XMLHttpRequest': 
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('enquirymessage')

		new_message = VehicleInquirie(vehicle=veh, customer_name=name, customer_email=email, customer_phone=phone, customer_message=message)
		new_message.save()
		
		response ={
			'name': name,
			'email': email,
			'phone': phone,
		}

		return JsonResponse(response)
	
	context = {
		'veh':veh,
	}
	return render(request,'vehicles/UsedCarDetails.html',context)


def usedVansPage(request):
	return render(request, 'vehicles/UsedVans.html')

def valetingPage(request):
	valets = Valet.objects.all()

	

	context = {
		'valets': valets,
	}
	return render(request, 'vehicles/Valeting.html',context)

def autoShinePage(request):
	return render(request, 'vehicles/AutoShine.html')

def contactUsPage(request):
	return render(request,'vehicles/Contact.html')

def sendMessage(request):
	if request.is_ajax():
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		new_message = Message(name=name, email=email, phone=phone, message=message)
		new_message.save()
		
		response ={
			'name': name,
			'email': email,
			'phone': phone,
		}

		return JsonResponse(response)


def sendValetEnquiry(request):
	# valet = Valet.objects.get(id=valet_id)

	if request.is_ajax():
		valet_id = request.POST.get('valet_id')
		valet = Valet.objects.get(id=valet_id)
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('valetenquirymessage')

		new_valet_enquiry = ValetEnquirie(valet=valet, customer_name=name, customer_email=email, customer_phone=phone, customer_message=message)
		new_valet_enquiry.save()
		
		response ={
			'name': name,
			'email': email,
			'phone': phone,
			'valet_id': valet_id,
		}

		return JsonResponse(response)