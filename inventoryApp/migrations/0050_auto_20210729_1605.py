# Generated by Django 3.2 on 2021-07-29 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0049_auto_20210729_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 16, 5, 38, 406238), null=True),
        ),
        migrations.AlterField(
            model_name='sellmodel',
            name='invoice',
            field=models.CharField(max_length=100),
        ),
    ]
