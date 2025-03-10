import uuid

from django.db import models


class WaypointType(models.TextChoices):
    PICKUP = 'PICKUP', 'Pickup'
    DELIVERY = 'DELIVERY', 'Delivery'

class TransportOrder(models.Model):
    order_number = models.CharField(max_length=100 , unique=True, null=False)
    customer_name = models.CharField(max_length=100, null=False)
    date = models.CharField(null=False , max_length=100)

    class Meta:
        db_table = 'transport-order'


class Waypoint(models.Model):
    waypoint_type = models.CharField(max_length=20, choices=WaypointType)
    address = models.CharField(max_length=100)

    transport_order = models.ForeignKey(
        TransportOrder,
        related_name='waypoints',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'waypoint'