from django.shortcuts import redirect, render, reverse
from .models import BlogPost
from .forms import BlogForm, EntryForm


def index(request):
    return render(request, 'blog/index.html')


def blogs(request):
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id) # show blogpost by id
    entries = blog.blogentry_set.order_by("-date_added")    # that - symbol reverse the entries
    context = {'blog': blog, 'entries': entries}

    return render(request, 'blog/blog.html', context)


def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()   # no data submited; create a blank form
    else:
        form = BlogForm(data=request.POST)  # use post when you want r-w
        if form.is_valid(): # check that all required fields have been filled in
            form.save() # write from form to the database
            return redirect('blog:blogs')
        
    context = {'form': form}

    return render(request, 'blog/new_blog.html', context)   # this execute when is blank or valid



def new_entry(request, blog_id):
    topic = BlogPost.objects.get(id=blog_id)
    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save() #write form into database
            return redirect('blog:blog', blog_id=blog_id)
    
    #display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'blog/new_entry.html', context)
