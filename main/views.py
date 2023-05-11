from django.shortcuts import render
from django.views.generic import ListView, DetailView
from  .models import Post
# Create your views here.
def index(request):
    return render(request, "main/index.html")

# def blog_view(request):
#     return render(request, "main/blog_view.html", {})

class blog_view(ListView):
    model = Post
    template_name = 'main/blog_view.html'

class blog_detail_view(DetailView):
    model = Post
    template_name = 'main/article.html'
