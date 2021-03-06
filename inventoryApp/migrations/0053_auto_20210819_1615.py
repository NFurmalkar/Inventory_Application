# Generated by Django 3.2 on 2021-08-19 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0052_alter_purchasemodel_purchasedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='returnpurchasemodel',
            old_name='custName',
            new_name='custNameId',
        ),
        migrations.RenameField(
            model_name='returnpurchasemodel',
            old_name='purchaseReturn',
            new_name='purchaseReturnId',
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 19, 16, 15, 10, 1913), null=True),
        ),
    ]
