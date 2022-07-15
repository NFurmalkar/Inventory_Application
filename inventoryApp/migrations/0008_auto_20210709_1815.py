# Generated by Django 3.2 on 2021-07-09 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0007_alter_purchasemodel_purchasedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='CGST',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='IGST',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 18, 15, 53, 763784)),
        ),
    ]