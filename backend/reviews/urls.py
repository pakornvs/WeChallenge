from django.urls import include, path

from backend.reviews.views import ReviewDetailUpdateView, ReviewListView, TagListView

urlpatterns = [
    path("reviews/", ReviewListView.as_view(), name="reviews"),
    path(
        "reviews/<pk>/", ReviewDetailUpdateView.as_view(), name="review-detail-update",
    ),
    path("tags/", TagListView.as_view(), name="tags"),
]
