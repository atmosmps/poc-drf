from tourist_place.models import TouristPlace
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer


class TouristPlaceSerializer(ModelSerializer):
    """
    Estabelece o relacionamento para permitir a listagem nested,
    aninhada, porém, caso seja necessário fazer um POST, a request também
    deverá ser feita passando o objeto inteiro, como Json por exemplo.
    """
    # from resource.api.serializers import ResourceSerializer
    # resource = ResourceSerializer(many=True)

    descricao_completa = SerializerMethodField()

    class Meta:
        model = TouristPlace
        fields = (
            'id',
            'name',
            'description',
            'image',
            'rating',
            'review',
            'address',
            'resource',
            'descricao_completa'
        )

    def get_descricao_completa(self, obj):
        """
        É possível no Serializer definir uma função com algum tipo de regra e
        tornar esta, um campo a ser retornado na resposta de maneira
        serializada. Isso é possível com o SerializerMethodField()

        https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield

        Não é muito recomendado colocar regras complexas aqui no Serializer

        É possível também usar propertys nos models, definindo o nome da
        property da mesma maneira que no serializer e passando nos fields
        do serializer
        """
        return f"{obj.name} - {obj.description}"
