from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from  .models import Post
from .forms import PostForm
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

class add_blog_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/add_blog.html'
    # fields = "__all__" #fields= ('title', 'title_tag')

def login(request):
    return render(request, 'main/login.html')