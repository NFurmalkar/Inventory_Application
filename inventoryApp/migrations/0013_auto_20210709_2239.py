# Generated by Django 3.2 on 2021-07-09 17:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0012_auto_20210709_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventoryApp.productmodel'),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 9, 22, 39, 45, 702754), null=True),
        ),
    ]
