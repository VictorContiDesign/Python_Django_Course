from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from website.forms import SignUpForm, BlogPostForm
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, "blog/base.html")

def signup(request):
    form = SignUpForm()  
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("home")
        else:
            form = SignUpForm()
    #form = SignUpForm()       
    return render(request, "accounts/signup.html", {"form":form})

def article(request):
    if request.method == "POST":  
        form = BlogPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            blog_post = form.save(commit=False)
            blog_post.published = True
            blog_post.save()
        return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            init_values["author"] = request.user
        init_values["date"] = datetime.today()
        form = BlogPostForm(initial=init_values)
    
    return render(request, "blog/article.html", {"form":form})