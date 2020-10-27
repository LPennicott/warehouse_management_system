from django.db import models
from django.urls import reverse

# Create your models here.

class Shipping_Units(models.Model):
    LOCATIONS = (
        ('JFK', 'JFK'),
        ('LAX', 'LAX'),
        ('ORD', 'ORD'),
    )
    locations = models.CharField(
        max_length=3,
        choices=LOCATIONS,
        default='JFK',
    )
    on_hand = models.AutoField(
        primary_key=True,
        editable=False,
    )
    shipper = models.CharField(max_length=50)
    consignee = models.CharField(max_length=50)
    width = models.PositiveIntegerField()
    length = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    gross_weight = models.PositiveIntegerField()
    remark = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    release_date = models.DateField(null=True, blank=True)
    hawb = models.CharField(max_length=50, null=True, blank=True)
    mawb = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey('CustomUser',
                             on_delete=models.CASCADE,
                             )

    class Meta:
        ordering = ('on_hand',)
        permissions = (
                       ('can_add_shipment', 'Can add a shipping unit'),
                       ('can_modify', 'Can modify a shipment'),
                       ('can_release', 'Can release a shipment'),
                       ('can_delete', 'Can erase a shipment from existence')
                    )

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse('unit_detail', args=[str(self.on_hand)])
