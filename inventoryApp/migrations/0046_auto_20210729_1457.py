# Generated by Django 3.2 on 2021-07-29 09:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0045_auto_20210729_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 14, 57, 51, 788960), null=True),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='customerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.customermodel'),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='stockId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.stockmodel'),
        ),
    ]
