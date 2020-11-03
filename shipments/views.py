from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import ShippingUnits, ShipmentImages
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

def shipment_list(request):
    shipments = ShippingUnits.objects.all()
    return render(request,
                  'shipments/shipment_list.html',
                  {'shipments': shipments})


def shipment_detail(request, pk):
    shipment = get_object_or_404(ShippingUnits, pk=pk)
    return render(request,
                  'shipments/shipment_detail.html',
                  {'shipment': shipment,
                   'images': ShipmentImages.objects.get(pk=shipment.pk)})
