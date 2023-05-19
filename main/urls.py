from django.urls import path
from . import views
from .views import blog_view, blog_detail_view, add_blog_post

urlpatterns = [
    path("", views.index, name="index"),
    # path("blog_view/", views.blog_view, name="blog_view")
    path("blog_view/", blog_view.as_view(), name="blog_view"),
    path('article/<int:pk>',  blog_detail_view.as_view(), name="article"),
    path('add_blog/', add_blog_post.as_view(), name="add_blog_post"),
    path('login/', views.login, name="login")
] 