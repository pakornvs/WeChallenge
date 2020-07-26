from django.db import models


class Review(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("reviews.Tag", related_name="reviews", editable=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.id


class Tag(models.Model):
    name = models.TextField(unique=True)
    searchable = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
