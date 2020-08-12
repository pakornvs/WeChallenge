from django.db.models import F, TextField, Value

from wechallenge.celery import app
from .models import Review, Tag


@app.task
def autotag_review(review_id):
    review = Review.objects.get(id=review_id)
    tags = Tag.objects.annotate(
        review_content=Value(review.content, output_field=TextField())
    ).filter(review_content__icontains=F("name"))
    review.tags.clear()
    review.tags.add(*tags)
