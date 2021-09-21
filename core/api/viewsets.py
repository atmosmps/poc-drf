from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import TouristPlaceSerializer
from core.models import TouristPlace


class TouristPlaceViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    serializer_class = TouristPlaceSerializer

    def get_queryset(self):
        return TouristPlace.objects.all()

    # detail=True, especifa que o pk/id do recurso que será acessado.
    # Caso contrário faz referência ao acesso global do recurso.
    @action(methods=['get'], detail=True)
    def report(self, request, pk=None):
        """/touristpoints/<pk>/report/"""
        pass
