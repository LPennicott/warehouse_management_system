from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import ShippingUnits, ShipmentImages
from .forms import ShipmentForm
from django.contrib.auth import get_user_model
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
    images = shipment.shipment_pics.all()
    return render(request,
                  'shipments/shipment_detail.html',
                  {'shipment': shipment,
                   'images': images})


def shipment_create(request):
    if request.method == 'GET':
        form = ShipmentForm()
        return render(request, 'shipments/shipment_create.html', {'form': form})
    else:
        form = ShipmentForm(request.POST)
        if form.is_valid():
            new_shipment = form.save(commit=False)
            new_shipment.user = request.user
            new_shipment.save()
            return redirect(new_shipment.get_absolute_url())


class UpdateShipmentView(UpdateView):
    model = ShippingUnits
    fields = ('locations', 'shipper', 'consignee', 'width', 'length', 'height',
              'gross_weight', 'unit_count', 'pallet_count', 'heat_treated_pallet_count',
              'remark', 'shipment_status')
    template_name = 'shipments/shipment_update.html'
