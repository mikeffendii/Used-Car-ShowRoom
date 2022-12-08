from django.contrib import admin

from .models import *

# Register your models here.


class VehicleImageAdmin(admin.StackedInline):
	model = VehicleImage

class VehicleInteriorAdmin(admin.StackedInline):
	model = VehicleInterior

class VehicleExteriorAdmin(admin.StackedInline):
	model = VehicleExterior

class VehicleSafetyAdmin(admin.StackedInline):
	model = VehicleSafety

class VehicleDimensionAdmin(admin.StackedInline):
	extra = 1
	max_num = 1
	model = VehicleDimension

class VehicleSummaryAdmin(admin.StackedInline):
	extra = 1
	max_num = 1
	model = VehicleSummary

class VehiclePerformanceEconomyAdmin(admin.StackedInline):
	extra = 1
	max_num = 1
	model = VehiclePerformanceEconomy

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
	inlines = [
		VehicleImageAdmin,
		VehicleInteriorAdmin,
		VehicleExteriorAdmin,
		VehicleSafetyAdmin,
		VehicleDimensionAdmin,
		VehicleSummaryAdmin,
		VehiclePerformanceEconomyAdmin,
	]

	class Meta:
		model = Vehicle

@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
	pass

admin.site.register(VehicleInterior)
admin.site.register(VehicleExterior)
admin.site.register(VehicleSummary)
admin.site.register(VehiclePerformanceEconomy)
admin.site.register(VehicleDimension)
admin.site.register(VehicleSafety)
admin.site.register(VehicleInquirie)
admin.site.register(Message)

admin.site.register(ValetFeature)
admin.site.register(ValetEnquirie)

class ValetFeatureAdmin(admin.StackedInline):
	model = ValetFeature
	
@admin.register(Valet)
class ValetAdmin(admin.ModelAdmin):
	inlines = [
		ValetFeatureAdmin
	]

	class Meta:
		model = Valet
