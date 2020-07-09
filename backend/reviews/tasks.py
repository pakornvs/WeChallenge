from celery import shared_task
from django.db.models import F, TextField, Value

from backend.reviews import models


@shared_task
def autotag_review(review_id):
    review = models.Review.objects.get(id=review_id)
    tags = models.Tag.objects.annotate(
        review_content=Value(review.content, output_field=TextField())
    ).filter(review_content__icontains=F("name"))
    review.tags.clear()
    review.tags.add(*tags)
