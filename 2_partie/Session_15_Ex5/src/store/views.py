from django.shortcuts import HttpResponse, get_object_or_404, render, HttpResponseRedirect
from .forms import AddBookForm
from datetime import datetime

from store.models import Book


def books(request): 
    form = AddBookForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        new_book = form.save(commit=False)
        new_book.published = True
        new_book.save()
    
    return render(request, "store/index.html", context={"books":Book.objects.all() , "form":form})


def book(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    return render(request, "store/book.html", context={"book":book})
