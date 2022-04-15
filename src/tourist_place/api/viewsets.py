from app.api.serializers import TouristPlaceSerializer
from app.models import TouristPlace
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class TouristPlaceViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    serializer_class = TouristPlaceSerializer

    """
    Habilita a busca por search e se baseia pelos campos definidos em
    "search_fields" para realizar a busca. Não é performático. Porém com esta
    definição de busca é possível utilizar os "lookup_prefixes" definidos em
    SearchFilter.
    """
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description')

    """
    Substitui o comportamento padrão de busca pelo id do model, e passa a
    realizar a busca principal pelo campo definido em "lookup_field", que por
    padrão é o ID do model.

    OBS: o campo definido em "lookup_field" precisa ser exclusivo(unique), caso
    contrário será retornado um exceção: MultipleObjectsReturned

    lookup_field = 'name'
    """

    """
    permission_classes = (IsAuthenticatedOrReadOnly,) por exemplo,
    só permite acesso a requsiões GET, para os demais métodos será
    necessario o token.
    """

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

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
