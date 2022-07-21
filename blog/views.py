from django.shortcuts import render, reverse
from .models import BlogPost
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')

def blogs(request):
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    
    return render(request, 'blog/blogs.html', context)



def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id) # show blogpost by id
    entries = blog.blogentry_set.order_by("-date_added") # that - symbol reverse the entries
    context = {'blog': blog, 'entries': entries}
    
    return render(request, 'blog/blog.html', context)