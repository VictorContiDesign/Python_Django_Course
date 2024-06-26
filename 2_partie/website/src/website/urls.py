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
from blog.views import blog_posts, blog_post
from .views import home, signup, article
from django.views import View

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('blog/', blog_posts, name="blog-index"),
    path('blog/<str:slug>/', blog_post, name="blog-post"),
    path('accounts/signup/', signup, name="signup"),
    path('article/', article, name="article")
]


