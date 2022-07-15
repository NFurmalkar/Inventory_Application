# Generated by Django 3.2 on 2021-07-28 18:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0033_auto_20210728_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='sellModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellDate', models.DateTimeField()),
                ('invoice', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('discount', models.FloatField()),
                ('CGST', models.FloatField()),
                ('IGST', models.FloatField()),
                ('taxableAmount', models.IntegerField()),
                ('totalAmount', models.BigIntegerField()),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.customermodel')),
                ('stockId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventoryApp.stockmodel')),
            ],
        ),
        migrations.AlterField(
            model_name='purchasemodel',
            name='purchaseDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 0, 3, 24, 675695), null=True),
        ),
        migrations.DeleteModel(
            name='salesDetailsModel',
        ),
    ]