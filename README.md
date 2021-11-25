# Django Rest Framework - Proof of Concept

## About

This is a project that aims to test some usage concepts, techniques and technologies.
The final idea is to understand the advantages and disadvantages of adopting them to solve real problems at jobs.

## The POC Project

## This project contain

- [X] Auth JWT Authetication
- [X] Open API Integration
- [ ] Automated tests
    - [ ] Integration tests
    - [ ] Unit tests
- [X] A modern dependence manager: Poetry
- [ ] Integrate to a external API
    - [ ] http://www.omdbapi.com/#usage
    - [ ] https://docs.github.com/en/rest
- [X] Deploy at Heroku
- [ ] Deploy at Heroku as Docker Container
- [ ] Dockerized app
- [ ] Use a CI service to deploy in heroku lke a gitlab CI

## TODO

- [ ] https://testdriven.io/blog/drf-views-part-3/
- [ ] Refactor endpoints
    - Add a Item endpoint
    - A Categorie contain many movies
    - A Item is a Autheticated endpint and categorie to

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

- https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html
- https://github.com/jazzband/djangorestframework-simplejwt
- https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje
- https://dev.to/aurelmegn/how-to-deploy-poetry-based-fast-api-on-heroku-2hd6
- https://python-poetry.org/docs/cli/
- https://klauslaube.com.br/2020/02/06/eu-me-rendo-django-rest-framework.html
- https://klauslaube.com.br/2020/12/30/poesia-pythonista-com-poetry.html
- https://klauslaube.com.br/2020/02/13/construindo-apis-em-django-com-django-rest-framework.html

## [Deploy Django App at Heroku](docs/deploy-django-app-at-heroku.md)

## [LICENSE](COPYING)
