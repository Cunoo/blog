
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'), # home page
    path('blogs/', views.blogs, name='blogs'), # view all blogs
    path('blogs/<int:blog_id>/', views.blog, name='blog'), # view given blog
]