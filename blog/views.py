from django.shortcuts import redirect, render, reverse
from django.urls import is_valid_path
from .models import BlogPost, BlogEntry
from .forms import BlogForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    return render(request, 'blog/index.html')

@login_required
def blogs(request):
    
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    
    return render(request, 'blog/blogs.html', context)

@login_required
def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id) # show blogpost by id
    if blog.owner != request.user: #   make sure the topic belongs to the current user
        raise Http404

    entries = blog.blogentry_set.order_by("-date_added")    # that - symbol reverse the entries
    context = {'blog': blog, 'entries': entries}

    return render(request, 'blog/blog.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()   # no data submited; create a blank form
    else:
        form = BlogForm(data=request.POST)  # use post when you want r-w
        if form.is_valid(): # check that all required fields have been filled in
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('blog:blogs')
        
    context = {'form': form}

    return render(request, 'blog/new_blog.html', context)   # this execute when is blank or valid


@login_required
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

@login_required
def edit_entry(request, entry_id):
    entry = BlogEntry.objects.get(id=entry_id)
    topic = entry.topic

    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry) #   initial reqquest, pre-fill form with the current entry
    else:
        #   post data submittd; proccess data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog', blog_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    
    return render(request, 'blog/edit_entry.html', context)
