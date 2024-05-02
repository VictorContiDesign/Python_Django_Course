"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import BlogIndexView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView
from .views import home, signup, HomeView, BlogPostCreateView

urlpatterns = [
    path('', HomeView.as_view(title="Acceuil du Blog"), name="home"),
    path('about', HomeView.as_view(title="A propos"), name="about"),
    path('admin/', admin.site.urls),
    path('blog/', BlogIndexView.as_view(), name="blog-index"),
    path('blog/create/', BlogPostCreateView.as_view(), name="create"),
    path('blog/<str:slug>/', BlogPostDetailView.as_view(), name="blog-post"),
    path('blog/<str:slug>/edit', BlogPostUpdateView.as_view(), name="blog-post-edit"),
    path('blog/<str:slug>/delete', BlogPostDeleteView.as_view(), name="blog-post-delete"),
    path('accounts/signup/', signup, name="signup"),   
]


