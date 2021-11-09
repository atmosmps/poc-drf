# Django Rest Framework - Proof of Concept

# About

This is a project that aims to test some usage concepts, techniques and technologies.
The final idea is to understand the advantages and disadvantages of adopting them to solve real problems at jobs.

# The POC Project

This POC is a "Feedly clone". [Feedly](https://feedly.com/) is a very popular kind of RSS reader (with steroids).

This project has two specific types: Channel and Item; *Channel* is actually the website or blog that we want to register
on our platform. This is the same name as the *RSS* format:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>RSS Title</title>
 <description>This is an example of an RSS feed</description>
 <link>https://www.example.com/main.html</link>
 <lastBuildDate>Mon, 06 Sep 2010 00:01:00 +0000 </lastBuildDate>
 <pubDate>Sun, 06 Sep 2009 16:20:00 +0000</pubDate>
 <ttl>1800</ttl>

 <item>
  <title>Example entry</title>
  <description>Here is some text containing an interesting description.</description>
  <link>https://www.example.com/blog/post/1</link>
  <guid isPermaLink="false">7bd204c6-1655-4c27-aeee-53f933c5395f</guid>
  <pubDate>Sun, 06 Sep 2009 16:20:00 +0000</pubDate>
 </item>

</channel>
</rss>
```

Already *Item*, as illustrated in the example above, is actually the news/article/music/podcast that that channel is
publishing.

# This project contain

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

# TODO

- [ ] https://testdriven.io/blog/drf-views-part-3/
- [ ] Refactor endpoints
    - Add a Item endpoint
    - A Categorie contain many movies
    - A Item is a Autheticated endpint and categorie to

# Positive points

- It’s a flexible and extensible toolkit used to build Web APIs in Django;
- Many libraries (maintained and stable) being maintained by the community;
- Features like the browseble api that make development easier;

# Negative points

- Django Framework overflow 
  - The Django Rest Framework works on top of the Django Framework layer, it is not an idenpendent library,
  but a layer library that allows you to build a Rest API using the Django framework;
- By choosing to use drf, the developer is stuck with the django ecosystem, not being able to choose to use modules
such as ORM other than the one provided by Django itself, for example.

# Articles used to help improve project

- https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html
- https://github.com/jazzband/djangorestframework-simplejwt
- https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje
- https://klauslaube.com.br/2020/02/06/eu-me-rendo-django-rest-framework.html
- https://dev.to/aurelmegn/how-to-deploy-poetry-based-fast-api-on-heroku-2hd6
- https://python-poetry.org/docs/cli/
- https://klauslaube.com.br/2020/12/30/poesia-pythonista-com-poetry.html
- 

# [Deploy Django App at Heroku](docs/deploy-django-app-at-heroku.md)

# [LICENSE](COPYING)
