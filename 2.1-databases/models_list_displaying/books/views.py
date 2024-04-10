from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        "books": [book for book in books]
    }
    return render(request, template, context)


def show_book(request, pub_date: str):
    paginator = Paginator(Book.pub_date.all(), 10)
    template = 'books/books_list.html'
    page = paginator.get_page(1)
    context = {
        "books": Book.objects.filter(pub_date=pub_date),
        "dates":
    }
    return render(request, template, context)
