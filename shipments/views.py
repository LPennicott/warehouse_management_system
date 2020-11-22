from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView

from .forms import ShipmentForm, ShipmentImageForm
from .models import ShippingUnits


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
                  {
                      'shipment': shipment,
                      'images': images
                  })


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


def image_add(request, pk):
    if request.method == 'POST':
        form = ShipmentImageForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES:
            shipment_image = get_object_or_404(ShippingUnits, pk=pk)
            if request.FILES['shipment_images'].name.split('.')[-1].lower() in (
            'jpeg', 'png', 'jpg'):
                new_image = form.save(commit=False)
                new_image.shipment = shipment_image
                new_image.save()
                return redirect(shipment_image.get_absolute_url())
            else:
                messages.warning(request,
                                 'Incorrect file type! Use "jpeg", "png" or '
                                 '"jpg"!')
                return redirect(shipment_image.get_absolute_url())
    else:
        form = ShipmentImageForm()
        shipment = get_object_or_404(ShippingUnits, pk=pk)
        return render(request, 'shipments/add_image.html',
                      {'form': form, 'shipment': shipment})


class UpdateShipmentView(UpdateView):
    model = ShippingUnits
    fields = ('locations', 'shipper', 'consignee', 'width', 'length', 'height',
              'gross_weight', 'unit_count', 'pallet_count',
              'heat_treated_pallet_count',
              'remark', 'shipment_status')
    template_name = 'shipments/shipment_update.html'


class DeleteShipmentView(DeleteView):
    model = ShippingUnits
    template_name = 'shipments/shipment_delete.html'
    success_url = reverse_lazy('shipments:shipment_list')
