from django.shortcuts import render
from django.views.generic import ListView
from posts.models import BlogPost

# Create your views here.
class BlogHome(ListView):
    model   = BlogPost
    context_object_name = "posts"
