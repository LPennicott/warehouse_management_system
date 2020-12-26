from django import template
from django.db.models import Sum
from ..models import ShippingUnits


register = template.Library()

@register.simple_tag
def unit_count():
    return ShippingUnits.objects.filter(release_date = None).count()

@register.simple_tag
def released_count():
    return ShippingUnits.objects.exclude(release_date = None).count()

@register.simple_tag
def in_house_weight():
	total_weight = ShippingUnits.objects.filter(release_date = None).aggregate(Sum('gross_weight'))
	return total_weight['gross_weight__sum']
