from rest_framework.viewsets import ModelViewSet
from review.api.serializers import ReviewSerializer
from review.models import Review


class ReviewViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
