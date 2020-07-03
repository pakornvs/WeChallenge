from django.test import TestCase
from rest_framework import generics
from rest_framework.test import APIRequestFactory

from backend.reviews.filters import ReviewSearchFilter
from backend.reviews.models import Review, Tag
from backend.reviews.serializers import ReviewSerializer
from backend.reviews.tasks import autotag_review
from backend.reviews.views import ReviewListView

factory = APIRequestFactory()


class ReviewListViewTest(TestCase):
    def setUp(self):
        self.search_keyword = "b"

        Tag(name=self.search_keyword).save()
        for idx in range(10):
            content = chr(idx + ord("a")) + chr(idx + ord("b")) + chr(idx + ord("c"))
            review = Review(content=content)
            review.save()
            autotag_review(review)

    def test_search(self):
        view = ReviewListView.as_view()
        request = factory.get("/", {"query": self.search_keyword})
        response = view(request)
        assert len(response.data["results"]) == 2
        assert response.data["results"][0]["content"] == "abc"
        assert response.data["results"][1]["content"] == "bcd"
