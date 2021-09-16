from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=2, decimal_places=2)
    created_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created_at = timezone.now()
        return super(Rating, self).save(*args, **kwargs)
