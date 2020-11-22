from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from .models import ShippingUnits, ShipmentImages


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = ShippingUnits
        fields = ('locations', 'shipper', 'consignee',
                  'width', 'length', 'height', 'gross_weight',
                  'unit_count', 'pallet_count', 'heat_treated_pallet_count',
                  'remark')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('locations', css_class='form-group col-md-2 mb-0'),
                Column('shipper', css_class='form-group col-md-5 mb-0'),
                Column('consignee', css_class='form-group col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('width', css_class='form-group col-md-4 mb-0'),
                Column('length', css_class='form-group col-md-4 mb-0'),
                Column('height', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('gross_weight', css_class='form-group col-md-3 mb-0'),
                Column('unit_count', css_class='form-group col-md-3 mb-0'),
                Column('pallet_count', css_class='form-group col-md-3 mb-0'),
                Column('heat_treated_pallet_count',
                       css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'remark',
            self.helper.add_input(Submit('submit', 'Create Shipment'))
        )

class ShipmentImageForm(forms.ModelForm):
    class Meta:
        model = ShipmentImages
        fields = ('shipment_images',)
