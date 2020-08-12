from rest_framework import serializers

from .models import Review, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        search_term = self.context.get("search_term")
        if search_term:
            ret["content"] = ret["content"].replace(
                search_term, f"<keyword>{search_term}</keyword>"
            )
        return ret

