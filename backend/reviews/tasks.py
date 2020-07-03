from django.db.models import F, TextField, Value

from backend.reviews.models import Tag


def autotag_review(review):
    tags = Tag.objects.annotate(
        review_content=Value(review.content, output_field=TextField())
    ).filter(review_content__icontains=F("name"))
    review.tags.add(*tags)
