from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Review, self).save(*args, **kwargs)
