from django.contrib import admin

from backend.reviews.models import Review, Tag


admin.site.register(Review)
admin.site.register(Tag)
