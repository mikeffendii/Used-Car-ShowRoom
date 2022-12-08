from django.db import models
import datetime


# Create your models here.
class Vehicle(models.Model):
    TRANSMISSION = (
		('Manual','Manual'),
		('Automatic','Automatic'),
		('Continuously variable','Continuously variable'),
		('Semi-automatic and dual-clutch','Semi-automatic and dual-clutch'),
		)
    FUELTYPE = (
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Bio-Diesel','Bio-Diesel'),
        ('Compressed Natural Gas (CNG)','Compressed Natural Gas (CNG)'),
    )
    name = models.CharField(max_length=40,null=False,default='No details available', help_text='Toyota yaris')
    short_description = models.TextField(max_length=500,default='No details available')
    long_description = models.TextField(max_length=900, default='No details available')
    price = models.CharField(max_length=255,null=False,default='No details available',help_text='')
    model_year = models.IntegerField(null=False,default='No details available', help_text='2017')
    fuel_type = models.CharField(max_length=40,default='No details available',null=False,choices=FUELTYPE)
    mileage = models.CharField(max_length=255,null=False,default='No details available',help_text='21,000')
    transmission = models.CharField(max_length=40,null=False,choices=TRANSMISSION,default='No details available')
    engine_size = models.CharField(max_length=40,null=False,default='No details available',help_text='2.7L')
    color = models.CharField(max_length=40,null=False)
    listed_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,upload_to="images/")


    def __str__(self):
    	return str(self.name)

class VehicleImage(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="images/")

	def __str__(self):
		return self.vehicle.name

class VehicleSummary(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	body_style = models.CharField(max_length=255, default='No details available',help_text='Hatchback')
	engine_size	= models.CharField(max_length=255, default='No details available', help_text='1299 cc')
	fuel_type =	models.CharField(max_length=255, default='No details available',help_text='Petrol')
	number_of_doors	= models.IntegerField( default='No details available',help_text='5 doors')
	number_of_seats	= models.IntegerField( default='No details available',help_text='5 seats')
	gearbox_type = models.CharField(max_length=255, default='No details available', help_text='semi-automatic')
	CO2_emissions = models.CharField(max_length=255, default='No details available', help_text='136 g/km')
	insurance_group	= models.CharField(max_length=255, default='No details available', help_text='06E')
	standard_manufacturer_warranty_miles = models.CharField(max_length=255, default='No details available', help_text='60000 miles')
	standard_manufacturer_warranty_years = models.CharField(max_length=255, default='No details available',help_text='4 years')
	standard_paintwork_guarantee = models.CharField(max_length=255, default='No details available',help_text='3 years')


	def __str__(self):
		return self.vehicle.name

class VehiclePerformanceEconomy(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	fuel_consumption_urban = models.CharField(max_length=250, default='No details available', help_text='42.2 mpg')
	fuel_consumption_extra_urban = models.CharField(max_length=250, default='No details available', help_text='42.2 mpg')
	fuel_consumption_combined = models.CharField(max_length=250, default='No details available', help_text='42.2 mpg')
	zero_to_sixty_mph = models.CharField(max_length=250, default='No details available', help_text =' 13.1 seconds')
	top_speed = models.CharField(max_length=250, default='No details available', help_text ='106 mph')
	cylinders = models.CharField(max_length=250, default='No details available', help_text ='4')
	valves = models.CharField(max_length=250, default='No details available', help_text ='16')
	engine_power = models.CharField(max_length=250, default='No details available', help_text ='85 bhp')
	engine_torque = models.CharField(max_length=250, default='No details available', help_text ='89.25 lbs/ft')

	def __str__(self):
		return self.vehicle.name


class VehicleDimension(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	height = models.CharField(max_length=250, default='No details available', help_text='1530 mm')
	height_inclusive_of_roof_rails = models.CharField(max_length=250, default='No details available', help_text='')
	length = models.CharField(max_length=250, default='No details available', help_text='1530 mm')
	wheelbase = models.CharField(max_length=250, default='No details available', help_text='2430 mm')
	width = models.CharField(max_length=250, default='No details available', help_text='1665 mm')
	width_icluding_mirrors = models.CharField(max_length=250, default='No details available', help_text='1960 mm')
	fuel_tank_capacity = models.CharField(max_length=250, default='No details available', help_text='42 litres')
	minimum_kerb_weight = models.CharField(max_length=250, default='No details available', help_text='1010 kg') 

	def __str__(self):
		return self.vehicle.name


class VehicleInterior(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	interior = models.CharField(max_length=250,default='No details available', help_text='Air-Conditioning')

	def __str__(self):
		return self.vehicle.name

class VehicleExterior(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	exterior = models.CharField(max_length=250,default='No details available', help_text='Spare Wheel')

	def __str__(self):
		return self.vehicle.name

class VehicleSafety(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	safety =  models.CharField(max_length=250,default='No details available', help_text='Air Bag')

	def __str__(self):
		return self.vehicle.name


class VehicleInquirie(models.Model):
	vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
	customer_name = models.CharField(max_length=250, default='Name', help_text='Your name')
	customer_email = models.EmailField(max_length=250)
	customer_phone = models.CharField(max_length=250, help_text='Phone')
	customer_message = models.TextField(help_text='Your message')
	inquiry_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.customer_name + ' | ' + self.vehicle.name + ' | ' + self.customer_phone

class Message(models.Model):
	name = models.CharField(max_length=250, help_text='Your name')
	email = models.EmailField(max_length=250)
	phone = models.CharField(max_length=250,help_text='Your phone number')
	message = models.TextField(help_text='Your message')
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


class Valet(models.Model):
	name = models.CharField(max_length=250, help_text='Mini valet')
	price = models.IntegerField(help_text='Valet price')

	def __str__(self):
		return self.name


class ValetFeature(models.Model):
	valet = models.ForeignKey(Valet,default=None, on_delete=models.CASCADE)
	feature = models.CharField(max_length=250, default='No details available', help_text='Valet feature')

	def __str__(self):
		return self.valet.name

		
class ValetEnquirie(models.Model):
	valet = models.ForeignKey(Valet,default=None,on_delete=models.CASCADE)
	customer_name = models.CharField(max_length=250, default='Name', help_text='Your name')
	customer_email = models.EmailField(max_length=250)
	customer_phone = models.CharField(max_length=250, help_text='Phone')
	customer_message = models.TextField(help_text='Your message')
	inquiry_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.customer_name + ' | ' + self.valet.name + ' | ' + self.customer_phone