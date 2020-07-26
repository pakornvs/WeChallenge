from django.urls import path

from .views import ReviewDetailUpdateView, ReviewSearchView, TagListView

urlpatterns = [
    path("api/reviews/", ReviewSearchView.as_view()),
    path("api/reviews/<pk>/", ReviewDetailUpdateView.as_view()),
    path("api/tags/", TagListView.as_view()),
]
