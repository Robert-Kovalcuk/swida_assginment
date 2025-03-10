# Generated by Django 5.1.7 on 2025-03-08 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransportOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=100, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'transport-order',
            },
        ),
        migrations.CreateModel(
            name='Waypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waypoint_type', models.CharField(choices=[('PICKUP', 'Pickup'), ('DELIVERY', 'Delivery')], max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('transport_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waypoints', to='swida_assignment.transportorder')),
            ],
            options={
                'db_table': 'waypoint',
            },
        ),
    ]
