from atexit import register
from django.contrib import admin
from .models import BlogEntry, BlogPost
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogEntry)