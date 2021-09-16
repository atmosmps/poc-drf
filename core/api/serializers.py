from rest_framework.serializers import ModelSerializer

from core.models import TouristPlace


class TouristPlaceSerializer(ModelSerializer):
    class Meta:
        model = TouristPlace
        fields = ['id', 'name', 'description']
