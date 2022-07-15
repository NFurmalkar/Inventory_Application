# Generated by Django 3.2 on 2021-07-28 18:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0024_auto_20210728_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 23, 45, 28, 141458), null=True),
        ),
        migrations.AlterField(
            model_name='salesdetailsmodel',
            name='customerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.customermodel'),
        ),
        migrations.AlterField(
            model_name='salesdetailsmodel',
            name='sellDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 23, 45, 28, 141458)),
        ),
        migrations.AlterField(
            model_name='salesdetailsmodel',
            name='stockId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.stockmodel'),
        ),
    ]