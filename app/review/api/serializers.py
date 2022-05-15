from rest_framework.serializers import ModelSerializer

from app.review.models import Review


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
