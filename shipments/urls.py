from django.urls import path

from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('shipments/<int:pk>', views.shipment_detail, name='shipment_detail'),
    path('shipments/create', views.shipment_create, name='shipment_create'),
    path('shipments/update/<int:pk>', views.UpdateShipmentView.as_view(),
         name='shipment_update'),
    path('shipments/delete/<int:pk>', views.DeleteShipmentView.as_view(),
         name='shipment_delete'),
    path('shipments/image_add/<int:pk>', views.image_add,
         name='shipment_image'),
]
