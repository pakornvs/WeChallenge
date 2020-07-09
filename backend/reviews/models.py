from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.reviews.tasks import autotag_review


class Review(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("reviews.Tag", related_name="reviews", editable=False)

    class Meta:
        ordering = ["id"]


class Tag(models.Model):
    name = models.TextField(unique=True)
    searchable = models.BooleanField(default=True)


@receiver(post_save, sender=Review)
def post_save_review_receiver(sender, instance, **kwargs):
    autotag_review.delay(review_id=instance.id)
