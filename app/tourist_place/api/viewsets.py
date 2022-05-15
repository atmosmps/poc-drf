from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.tourist_place.api.serializers import TouristPlaceSerializer
from app.tourist_place.models import TouristPlace


class TouristPlaceViewSet(ModelViewSet):
    serializer_class = TouristPlaceSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name", "description")
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        id = self.request.query_params.get("id", None)
        name = self.request.query_params.get("name", None)
        description = self.request.query_params.get("description", None)

        queryset = TouristPlace.objects.all()

        if id:
            queryset = queryset.filter(pk=id)
        if name:
            queryset = queryset.filter(name__iexact=name)
        if description:
            queryset = queryset.filter(description__iexact=description)
        return queryset

    @action(methods=["get"], detail=True)
    def report(self, request, pk=None):
        """/touristpoints/<pk>/report/"""
        pass
