from django.contrib import admin

from .models import ShippingUnits, ShipmentImages


# Register your models here.

class ShippingUnitAdmin(admin.ModelAdmin):
    list_display = ['on_hand', 'locations', 'shipper', 'gross_weight',
                    'create_date',
                    'hawb', 'mawb', ]


class ShipmentImageAdmin(admin.ModelAdmin):
    list_display = ['shipment', 'shipment_images']


admin.site.register(ShippingUnits, ShippingUnitAdmin)
admin.site.register(ShipmentImages, ShipmentImageAdmin)
