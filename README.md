# Django Rest Framework - Proof of Concept

## About

This is a project that aims to test some usage concepts, techniques and technologies.
The final idea is to understand the advantages and disadvantages of adopting them to solve real problems at jobs.

## The POC Project

## About

This project contain three apps:

- location: to consult your actual location;

## This project contain

- [X] Auth JWT Authetication
- [X] Open API Integration
- [X] Automated tests
    - [X] Integration tests
    - [X] Unit tests
- [X] A modern dependence manager: Poetry
- [X] Integrate to a external API
    - [X] https://ipstack.com/documentation
- [X] Deploy at Heroku
- [X] Config Makefile
- [X] Pytest with coverage

## Dockerized app

*OBS: A lot of changes would be needed here, and this would remove almost all content about traditional deployment using Heroku, so the deploy configurations with docker, were done in this other project:*

- [ ] Deploy at Heroku as Docker Container.
- [ ] Use a CI service to deploy in heroku lke a gitlab CI
- [ ] Dockerized app

## TODO

- [ ] Define Autheticated endpoints
- [ ] Add documentation to run project

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

## [Deploy Django App at Heroku](docs/deploy-django-app-at-heroku.md)

## [LICENSE](COPYING)
