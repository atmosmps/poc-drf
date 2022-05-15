# POC Notes

## Notas do projeto

```
"""
Estabelece o relacionamento para permitir a listagem nested,
aninhada, porém, caso seja necessário fazer um POST, a request também
deverá ser feita passando o objeto inteiro, como Json por exemplo.
"""
# from resource.api.serializers import ResourceSerializer
# resource = ResourceSerializer(many=True)
```

```
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
```

```
"""
Habilita a busca por search e se baseia pelos campos definidos em
"search_fields" para realizar a busca. Não é performático. Porém com esta
definição de busca é possível utilizar os "lookup_prefixes" definidos em
SearchFilter.
"""
filter_backends = (SearchFilter,)
search_fields = ("name", "description")

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
```

```
# detail=True, especifa que o pk/id do recurso que será acessado.
# Caso contrário faz referência ao acesso global do recurso.
@action(methods=["get"], detail=True)
```

## Positive points

- It’s a flexible and extensible toolkit used to build Web APIs in Django;
- Many libraries (maintained and stable) being maintained by the community;
- Features like the browseble api that make development easier;

## Negative points

- Django Framework overflow 
    - The Django Rest Framework works on top of the Django Framework layer, it is not an idenpendent library,
    but a layer library that allows you to build a Rest API using the Django framework;
- By choosing to use drf, the developer is stuck with the django ecosystem, not being able to choose to use modules
such as ORM other than the one provided by Django itself, for example.

## Articles used to help improve project

- https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
- https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html
- https://github.com/jazzband/djangorestframework-simplejwt
- https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje
- https://dev.to/aurelmegn/how-to-deploy-poetry-based-fast-api-on-heroku-2hd6
- https://klauslaube.com.br/2020/12/30/poesia-pythonista-com-poetry.html
- https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
- https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html#basic-example-geo-location-api

## [Deploy Django App at Heroku](deploy-django-app-at-heroku.md)
