from django.urls import path

from backend.reviews.views import ReviewDetailUpdateView, ReviewListView, TagListView

urlpatterns = [
    path("reviews/", ReviewListView.as_view()),
    path("reviews/<pk>/", ReviewDetailUpdateView.as_view()),
    path("tags/", TagListView.as_view()),
]
