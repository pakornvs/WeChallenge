from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

from .models import Review, Tag
from .serializers import ReviewSerializer, TagSerializer
from .tasks import autotag_review


class ReviewDetailUpdateView(RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)


class ReviewSearchView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)

    def filter_queryset(self, queryset):
        search_term = self.request.query_params.get("query", None)
        if search_term is not None:
            return queryset.filter(
                tags__searchable=True, tags__name__iexact=search_term
            )

        return queryset.none()


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


@receiver(post_save, sender=Review)
def post_save_review_receiver(sender, instance, **kwargs):
    autotag_review.delay(instance.id)

