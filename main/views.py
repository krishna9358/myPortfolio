from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def blog_view(request):
    return render(request, "main/blog_view.html", {})