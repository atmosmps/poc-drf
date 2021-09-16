from rest_framework.viewsets import ModelViewSet

from rating.api.serializers import RatingSerializer
from rating.models import Rating


class RatingViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
