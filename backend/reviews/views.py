from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

from .models import Review, Tag
from .serializers import ReviewSerializer, TagSerializer


class ReviewDetailUpdateView(RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)


class ReviewSearchView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"search_term": self.search_term})
        return context

    def filter_queryset(self, queryset):
        self.search_term = self.request.query_params.get("query", None)
        if self.search_term:
            queryset = queryset.filter(tags__name__iexact=self.search_term)
        return queryset


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
