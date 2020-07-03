from rest_framework.filters import BaseFilterBackend

from backend.reviews.models import Tag


class ReviewSearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search_term = request.query_params.get("query", None)
        if search_term is not None:
            queryset = queryset.filter(
                tags__searchable=True, tags__name__iexact=search_term
            )
        return queryset
