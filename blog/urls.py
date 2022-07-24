
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'), # home page
    path('blogs/', views.blogs, name='blogs'), # view all blogs
    path('blogs/<int:blog_id>/', views.blog, name='blog'), # view given blog
    path('new_blog/', views.new_blog, name='new_blog'), # create new blog in html
    path('new_entry/<int:blog_id>/', views.new_entry, name='new_entry'), # for adding new entry in html
]