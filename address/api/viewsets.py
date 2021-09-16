from rest_framework.viewsets import ModelViewSet

from address.api.serializers import AddressPlaceSerializer
from address.models import Address


class AddressViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = Address.objects.all()
    serializer_class = AddressPlaceSerializer
