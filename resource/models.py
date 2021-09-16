from django.db import models
from django.utils import timezone


class Resource(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    minimum_age = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Resource, self).save(*args, **kwargs)
