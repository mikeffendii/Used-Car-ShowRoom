from django.urls import path
from .views import *
from . import views


urlpatterns = [
    # path('usedcarss/',VehicleListView.as_view(),name = 'usedcarpage'),
    path('', views.homePage, name='homepage'),
    path('UsedCars/', views.usedCarsPage, name='usedcarspage'),
    path('CarDetails/<int:veh_id>/', views.usedCarDetailPage, name='usedcarsdetailspage'),
    path('UsedVans/', views.usedVansPage, name='usedvanspage'),
    path('Valeting/', views.valetingPage, name='valetingpage'),
    path('AutoShine/', views.autoShinePage, name='autoshinepage'),
    path('ContactUs/', views.contactUsPage, name='contactpage'),
    path('sendMessage/', sendMessage, name='sendMessage'),
    path('sendValetEnquiry/', sendValetEnquiry, name='sendValetEnquiry'),
]