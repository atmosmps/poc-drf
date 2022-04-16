from app.review.api.serializers import ReviewSerializer
from app.review.models import Review
from rest_framework.viewsets import ModelViewSet


class ReviewViewSet(ModelViewSet):
    """A simple ViewSet for viewing and editing accounts."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
