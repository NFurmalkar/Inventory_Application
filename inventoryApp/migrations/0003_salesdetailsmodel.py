# Generated by Django 3.2 on 2021-06-28 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0002_productmodel_purchasemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='salesDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.productmodel')),
            ],
        ),
    ]
