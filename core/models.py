from django.db import models
from resources.models import Resource


class TouristPlaces(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.name
