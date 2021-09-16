from rest_framework.viewsets import ModelViewSet

from core.api.serializers import TouristPlaceSerializer
from core.models import TouristPlace


class TouristPlaceViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = TouristPlace.objects.all()
    serializer_class = TouristPlaceSerializer
