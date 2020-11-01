from django.db import models

# Create your models here.

class Consols(models.Model):
    create_date = models.DateField(auto_now_add=True)
    mawb = models.CharField(max_length=13, primary_key=True)
    client = models.CharField(max_length=50)
    cutoff = models.DateField()
    destination = models.CharField(max_length=4)
    shipment_status = models.BooleanField(default=True)

    class Meta:

        verbose_name = 'Consol'
