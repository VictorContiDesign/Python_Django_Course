from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from blog.models import BlogPost
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
'''
def blog_post(request):
    r = HttpResponse()
    r["Content-Type"] = "application/json"
    r.content = "Bonjour tout le monde"
    print(type(r.content))
    return r
'''

'''
def blog_post(request):
    return JsonResponse({"1" : "Premier article du blog"})
'''
    
'''
def blog_post(request):
    try:
        blog_art = BlogPost.objects.get(pk=3)
    except BlogPost.DoesNotExist:
        raise Http404("L'article #1 n'existe pas")
    
    return HttpResponse(blog_art.content)
'''

'''    
def blog_posts(request):
    #return HttpResponse("Tous les articles du blog")
    return redirect("home")
'''

'''
def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    #response = HttpResponse(post.content)
    #response = HttpResponse(render_to_string("blog/post.html", context={"blog_post" : post}))
    response = render(request, "blog/post.html", context={"blog_post" : post})
    return response
'''

'''
@login_required
def blog_posts(request):
    post = get_object_or_404(BlogPost, pk=3)
    return HttpResponse(post.content)
'''
    
'''
@user_passes_test(lambda u: u.username == "Victor")
def blog_posts(request):
    post = get_object_or_404(BlogPost, pk=3)
    return HttpResponse(post.content)
'''

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/post.html", context={"post" : post})

def blog_posts(request):
    #posts = BlogPost.objects.filter(pk__in=[1, 2, 3, 4, 5])
    #posts = BlogPost.objects.filter(pk__in=[6, 7, 8, 9, 10])
    #posts = BlogPost.objects.filter(pk__in=[20, 21, 22])
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", context={"posts" : posts})

