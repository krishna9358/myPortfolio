from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog_view/", views.blog_view, name="blog_view")
]