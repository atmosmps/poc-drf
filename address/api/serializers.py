from rest_framework.serializers import ModelSerializer

from address.models import Address


class AddressPlaceSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'line1',
            'line2',
            'city',
            'state',
            'state_abbreviation',
            'country',
            'latitude',
            'longitude',
            'created_at',
            'updated_at'
        ]
