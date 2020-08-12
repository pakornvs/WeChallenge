from django.urls import path

from .views import ReviewDetailUpdateView, ReviewSearchView, TagListView

urlpatterns = [
    path("reviews/", ReviewSearchView.as_view()),
    path("reviews/<pk>/", ReviewDetailUpdateView.as_view()),
    path("tags/", TagListView.as_view()),
]
