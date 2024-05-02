from django.shortcuts import HttpResponse, get_object_or_404, render

from store.models import Book


def books(request):
    books = Book.objects.all()
    return render(request, "store/index.html", context={"books":books})


def book(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    return render(request, "store/book.html", context={"book":book})
