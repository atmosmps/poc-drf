from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from app.tourist_place.models import TouristPlace


class TouristPlaceSerializer(ModelSerializer):
    descricao_completa = SerializerMethodField()

    class Meta:
        model = TouristPlace
        fields = (
            "id",
            "name",
            "description",
            "image",
            "review",
            "descricao_completa",
        )

    def get_descricao_completa(self, obj):
        return f"{obj.name} - {obj.description}"
