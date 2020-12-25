# Generated by Django 3.1.2 on 2020-11-03 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0003_auto_20201101_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentimages',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment_pics', to='shipments.shippingunits'),
        ),
        migrations.AlterField(
            model_name='shipmentimages',
            name='shipment_images',
            field=models.ImageField(blank=True, null=True, upload_to='shipments_images/'),
        ),
    ]
