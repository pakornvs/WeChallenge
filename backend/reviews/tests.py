from django.test import TestCase
from rest_framework.test import APIRequestFactory

from .models import Review, Tag
from .tasks import autotag_review
from .views import ReviewSearchView

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
        view = ReviewSearchView.as_view()
        request = factory.get("/", {"query": self.search_keyword})
        response = view(request)
        results = response.data["results"]
        assert len(results) == 2
        assert results[0]["content"] == "abc"
        assert results[1]["content"] == "bcd"
