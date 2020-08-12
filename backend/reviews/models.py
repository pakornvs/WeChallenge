from django.db import models
from django.utils.html import escape


class Tag(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="reviews", editable=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id

