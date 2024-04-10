from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def index(request: str):
    return redirect('books')


def books_view(request: str):
    template = 'books/books_list.html'
    books = Book.objects.all()

    context = {
        "books": [book for book in books]
    }
    return render(request, template, context)


def show_book(request: str, pub_date: str):
    paginator = Paginator(Book.objects.order_by("pub_date"), 10)

    paginator = Paginator({str(book.pub_date) for book in Book.objects.all()}, 1)
    template = 'books/pub_date.html'


    context = {
        "books": [book for book in Book.objects.filter(pub_date=pub_date).all()],
        # "dates": [prev_page, next_page]
    }
    return render(request, template, context)
# {% endfor %}
#             {% if page.has_previous%}
#             <a href="/{{}}">{{}}</a>
#             {% endif %}
#             {% if page.has_next%}
#             <a href="/{{}}">{{}}</a>
#             {% endif %}