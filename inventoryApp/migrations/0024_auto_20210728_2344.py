# Generated by Django 3.2 on 2021-07-28 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0023_auto_20210728_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 23, 44, 3, 136111), null=True),
        ),
        migrations.AlterField(
            model_name='salesdetailsmodel',
            name='sellDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 23, 44, 3, 136111)),
        ),
    ]