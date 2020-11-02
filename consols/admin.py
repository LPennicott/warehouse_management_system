from django.contrib import admin
from .models import Consols
# Register your models here.

class ConsolsAdmin(admin.ModelAdmin):
    model = Consols
    list_display = ['mawb', 'destination', 'create_date', 'shipment_status']

admin.site.register(Consols, ConsolsAdmin)
