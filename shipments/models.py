import datetime

from django.db import models
from django.urls import reverse


# Create your models here.


class ShippingUnits(models.Model):
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
    unit_count = models.PositiveIntegerField()
    pallet_count = models.PositiveIntegerField()
    heat_treated_pallet_count = models.PositiveIntegerField()
    remark = models.TextField()
    shipment_status = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)
    release_date = models.DateField(null=True, blank=True)
    hawb = models.ForeignKey('consols.Consols',
                             on_delete=models.CASCADE,
                             related_name='hawbs',
                             null=True, blank=True)
    mawb = models.ForeignKey('consols.Consols',
                             on_delete=models.CASCADE,
                             related_name='mawbs',
                             null=True, blank=True)
    user = models.ForeignKey('users.CustomUser',
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
        verbose_name = 'Shipping Unit'

    def __str__(self):
        return f'{self.on_hand} - {self.shipper}'

    def get_absolute_url(self):
        return reverse('shipments:shipment_detail', args=[str(self.on_hand)])

    def volume_weight(self):
        return (self.length * self.width * self.height) / 366

    def gross_weight_to_kg(self):
        return round(self.gross_weight / 2.204, 2)

    def cbm(self):
        pass

    def identifier(self):
        return (str(self.locations) + "-" + str(self.on_hand))

    def days_in_house(self):
        return str(datetime.date.today() - self.create_date).split(',')[0]


class ShipmentImages(models.Model):
    shipment = models.ForeignKey(ShippingUnits, on_delete=models.CASCADE,
                                 related_name='shipment_pics')
    shipment_images = models.ImageField(upload_to='shipments_images/',
                                        blank=True,
                                        null=True)

    class Meta:
        verbose_name = 'Shipment Image'
