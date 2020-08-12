from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Review
from .tasks import autotag_review


@receiver(post_save, sender=Review)
def post_save_review(sender, instance, **kwargs):
    autotag_review.delay(instance.id)
