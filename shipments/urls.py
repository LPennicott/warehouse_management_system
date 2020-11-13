from django.urls import path

from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('shipments/<int:pk>', views.shipment_detail, name='shipment_detail'),
    path('shipments/create', views.shipment_create, name='shipment_create'),
]
