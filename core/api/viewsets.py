from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import TouristPlaceSerializer
from core.models import TouristPlace


class TouristPlaceViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    serializer_class = TouristPlaceSerializer

    def get_queryset(self):
        id = self.request.query_params.get['id', None]
        name = self.request.query_params.get['name', None]
        description = self.request.query_params.get['description', None]

        queryset = TouristPlace.objects.all()

        if id:
            queryset = queryset.filter(pk=id)
        if name:
            queryset = queryset.filter(name__iexact=name)
        if description:
            queryset = queryset.filter(description__iexact=description)
        return queryset

    # detail=True, especifa que o pk/id do recurso que será acessado.
    # Caso contrário faz referência ao acesso global do recurso.
    @action(methods=['get'], detail=True)
    def report(self, request, pk=None):
        """/touristpoints/<pk>/report/"""
        pass
