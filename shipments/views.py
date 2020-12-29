from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Sum
from django.views.generic import (
    TemplateView,
    UpdateView,
    DeleteView,
    ListView,
    CreateView,
)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from .forms import ShipmentForm, ShipmentImageForm, ConsolidationForm
from .models import ShippingUnits, Consols


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


def shipment_list(request):
    shipments = ShippingUnits.objects.all()
    return render(
        request, "shipments/shipment_list.html", {"shipments": shipments}
    )


def shipment_detail(request, pk):
    shipment = get_object_or_404(ShippingUnits, pk=pk)
    images = shipment.shipment_pics.all()
    return render(
        request,
        "shipments/shipment_detail.html",
        {"shipment": shipment, "images": images},
    )


def shipment_create(request):
    if request.method == "GET":
        form = ShipmentForm()
        return render(
            request, "shipments/shipment_create.html", {"form": form}
        )
    else:
        form = ShipmentForm(request.POST)
        if form.is_valid():
            new_shipment = form.save(commit=False)
            new_shipment.user = request.user
            new_shipment.save()
            return redirect(new_shipment.get_absolute_url())


def image_add(request, pk):
    if request.method == "POST":
        form = ShipmentImageForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES:
            shipment_image = get_object_or_404(ShippingUnits, pk=pk)
            if request.FILES["shipment_images"].name.split(".")[
                -1
            ].lower() in ("jpeg", "png", "jpg"):
                new_image = form.save(commit=False)
                new_image.shipment = shipment_image
                new_image.save()
                return redirect(shipment_image.get_absolute_url())
            else:
                messages.warning(
                    request,
                    'Incorrect file type! Use "jpeg", "png" or ' '"jpg"!',
                )
                return redirect(shipment_image.get_absolute_url())
    else:
        form = ShipmentImageForm()
        shipment = get_object_or_404(ShippingUnits, pk=pk)
        return render(
            request,
            "shipments/add_image.html",
            {"form": form, "shipment": shipment},
        )


class UpdateShipmentView(UpdateView):
    model = ShippingUnits
    fields = (
        "locations",
        "shipper",
        "consignee",
        "width",
        "length",
        "height",
        "gross_weight",
        "unit_count",
        "pallet_count",
        "heat_treated_pallet_count",
        "remark",
        "shipment_status",
    )
    template_name = "shipments/shipment_update.html"
    context_object_name = "shipment"


class DeleteShipmentView(DeleteView):
    model = ShippingUnits
    template_name = "shipments/shipment_delete.html"
    success_url = reverse_lazy("shipments:shipment_list")


class CreateConsolView(LoginRequiredMixin, CreateView):
    model = Consols
    template_name = "shipments/new_consolidation.html"
    form_class = ConsolidationForm
    login_url = "account_login"


class Consolidation(LoginRequiredMixin, ListView):
    model = Consols
    template_name = "shipments/consolidation_list.html"
    login_url = "account_login"
    context_object_name = "consols"
    success_url = reverse_lazy("shipments:consolidation_list")


def consoldation_shipments(request, pk):
    mawb_selection = get_object_or_404(Consols, mawb=pk)
    shipments = ShippingUnits.objects.filter(mawb=None)
    if request.method == "POST":
        consol_form = ConsolidationForm(request.POST)
        units = request.POST.getlist("onhands[]")
        ShippingUnits.objects.filter(on_hand__in=units).update(
            mawb=mawb_selection.mawb
        )
        return redirect("shipments:consolidation_list")
    else:
        consol_form = ConsolidationForm()
        return render(
            request,
            "shipments/consolidation_update.html",
            {
                "form": consol_form,
                "mawb": mawb_selection,
                "shipments": shipments,
            },
        )


def consol_detail(request, pk):
    consol = get_object_or_404(Consols, mawb=pk)
    shipments = consol.mawbs.all()
    return render(
        request,
        "shipments/consol_detail.html",
        {"consol": consol, "shipments": shipments,},
    )


def remove_shipments_from_consol(request, pk):
    if request.method == "POST":
        units = request.POST.getlist("onhands[]")
        ShippingUnits.objects.filter(on_hand__in=units).update(mawb=None)
        return redirect("shipments:consol_detail", pk=pk)


class UpdateConsolView(UpdateView):
    model = Consols
    fields = ("mawb", "cutoff", "destination")
    context_object_name = "consol"
    template_name = "shipments/consol_update.html"
