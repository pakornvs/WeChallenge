from rest_framework import serializers

from backend.reviews.models import Review, Tag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ("id", "content", "created", "updated")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
