from rest_framework import serializers

from swida_assignment.models import TransportOrder, Waypoint


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['id', 'waypoint_type', 'address']

class TransportOrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True)

    class Meta:
        model = TransportOrder
        fields = ['id', 'order_number', 'customer_name', 'date', 'waypoints']


    def create(self, validated_data):
        waypoints_data = validated_data.pop('waypoints', [])
        transport_order = TransportOrder.objects.create(**validated_data)

        for waypoint_data in waypoints_data:
            Waypoint.objects.create(transport_order=transport_order, **waypoint_data)

        return transport_order

    def validate(self, data):
        self.order_should_pickup_and_deliver(data)

        return data

    @staticmethod
    def order_should_pickup_and_deliver(data):
        waypoints_data = data.get('waypoints', [])

        pickup = any(item.get('waypoint_type') == 'PICKUP' for item in waypoints_data)
        delivery = any(item.get('waypoint_type') == 'DELIVERY' for item in waypoints_data)

        if not (pickup and delivery):
            raise serializers.ValidationError(
                "TransportOrder must have at least one pickup and one delivery waypoint."
            )

