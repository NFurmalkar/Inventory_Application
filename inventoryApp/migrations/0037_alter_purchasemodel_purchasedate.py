# Generated by Django 3.2 on 2021-07-28 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0036_alter_purchasemodel_purchasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 0, 23, 15, 384949), null=True),
        ),
    ]
