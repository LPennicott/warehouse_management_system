from django.shortcuts import render, get_object_or_404
from .models import ShippingUnits
# Create your views here.


def shipment_list(request):
    shipments = ShippingUnits.objects.all()
    return render(request,
                  'shipments/shipment_list.html',
                  {'shipments': shipments})
