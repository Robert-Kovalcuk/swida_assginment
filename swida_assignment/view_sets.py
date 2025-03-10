from rest_framework import viewsets

from swida_assignment.models import TransportOrder, Waypoint
from swida_assignment.serializers import TransportOrderSerializer, WaypointSerializer


class TransportOrderViewSet(viewsets.ModelViewSet):
    queryset = TransportOrder.objects.all()
    serializer_class = TransportOrderSerializer

    def get_queryset(self):
        customer_name = self.request.query_params.get('customer_name')

        if customer_name:
            return TransportOrder.objects.filter(customer_name=customer_name)

        return TransportOrder.objects.all()


class WaypointViewSet(viewsets.ModelViewSet):
    queryset = Waypoint.objects.all()
    serializer_class = WaypointSerializer