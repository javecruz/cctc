# Generated by Django 2.2.5 on 2019-09-16 15:45

import ShopManagement.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[(ShopManagement.models.CountryEnum('SPAIN'), 'SPAIN'), (ShopManagement.models.CountryEnum('PORTUGAL'), 'PORTUGAL'), (ShopManagement.models.CountryEnum('FRANCE'), 'FRANCE')], default=ShopManagement.models.CountryEnum('SPAIN'), max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('isReady', models.BooleanField(default=False)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManagement.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManagement.Order')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManagement.Product')),
            ],
        ),
    ]
