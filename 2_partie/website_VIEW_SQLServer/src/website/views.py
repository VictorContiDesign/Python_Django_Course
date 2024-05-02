from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import BlogPost
from website.forms import SignUpForm, BlogPostForm
from datetime import datetime
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


# Create your views here.
class HomeView(TemplateView):
    template_name = "blog/base.html"
    title = "Default"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

'''
class HomeView(View):
    def get(self, request):
        return render(request, "blog/base.html")
'''
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

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/create.html"
    # fields = ["title", "author", "content"]
    form_class = BlogPostForm
    # success_url = reverse_lazy("blog-index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Créer"
        return context
    
    def get_success_url(self) -> str:
        return reverse("blog-index")
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        
        form.instance.published = True
        
        return super().form_valid(form)

def create(request):
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
    
    return render(request, "blog/create.html", {"form":form})
