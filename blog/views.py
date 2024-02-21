from django.shortcuts import render
from blog.models import Blogs

# Create your views here.
def blogview(request, *args, **kwargs):
    blog = Blogs.objects.all().order_by("title")
    return render(request, "blog/blog.html", {"blogs": blog})