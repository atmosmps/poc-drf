from rest_framework.viewsets import ModelViewSet

from app.review.api.serializers import ReviewSerializer
from app.review.models import Review


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
