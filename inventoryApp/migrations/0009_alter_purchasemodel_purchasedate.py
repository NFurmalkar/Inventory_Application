# Generated by Django 3.2 on 2021-07-09 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0008_auto_20210709_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
