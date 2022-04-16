from app.review.models import Review
from rest_framework.serializers import ModelSerializer


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "review",
            "date",
            "approved",
            "created_at",
            "updated_at",
        ]
