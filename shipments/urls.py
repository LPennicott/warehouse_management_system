from django.urls import path

from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.shipment_list, name='shipments'),
]
