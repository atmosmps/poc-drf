from rest_framework.serializers import ModelSerializer

from resource.models import Resource


class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            'id', 'name', 'description', 'opening_time', 'closing_time',
            'minimum_age', 'created_at'
        ]
