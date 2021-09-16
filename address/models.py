from django.db import models
from django.utils import timezone


class Address(models.Model):
    # TODO: melhorar estrutura de enderecos para contemplar mais possiblidades
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10, default=u'Maranhão')
    state_abbreviation = models.CharField(max_length=2, default=u'MA')
    country = models.CharField(max_length=6, default=u'Brasil')
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.line1
    
    def save(self, *args, **kwargs):
        """On save, update timestamps."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Address, self).save(*args, **kwargs)
