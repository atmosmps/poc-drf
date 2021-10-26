from rest_framework.viewsets import ModelViewSet

from resource.api.serializers import ResourceSerializer
from resource.models import Resource


class ResourceViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_fields = ('name', 'description')
