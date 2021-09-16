from django.db import models
from django.utils import timezone

from address.models import Address
from rating.models import Rating
from resource.models import Resource
from review.models import Review


class TouristPlace(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    resource = models.ManyToManyField(Resource)
    review = models.ManyToManyField(Review)
    rating = models.ManyToManyField(Rating)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(TouristPlace, self).save(*args, **kwargs)
