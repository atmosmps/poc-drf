from rest_framework.viewsets import ModelViewSet

from core.api.serializers import TouristPlaceSerializer
from core.models import TouristPlace


class TouristPlaceViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    serializer_class = TouristPlaceSerializer

    def get_queryset(self):
        return TouristPlace.objects.all()


