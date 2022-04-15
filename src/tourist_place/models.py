from django.db import models
from django.utils import timezone
from review.models import Review


class TouristPlace(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    review = models.ManyToManyField(Review)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='tourist_place', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(TouristPlace, self).save(*args, **kwargs)
