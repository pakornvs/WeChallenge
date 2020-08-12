from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("reviews.urls")),
    path("", TemplateView.as_view(template_name="index.html")),
    re_path(".*/$", TemplateView.as_view(template_name="index.html")),
]
