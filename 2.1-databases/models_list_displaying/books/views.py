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
    dates = Book.objects.distinct("pub_date").order_by("pub_date")

    paginator = Paginator(dates, 1)
    template = 'books/pub_date.html'
    books = [book for book in Book.objects.filter(pub_date=pub_date).all()]
    for book in books:
        book.pub_date = str(book.pub_date)
    context = {
        "books": books,
    }
    for page in paginator:
        if pub_date == str(list(page.object_list)[0].pub_date):
            context.update({"page": page, "current_page": str(paginator.get_page(page.number).object_list[0].pub_date)})
            if page.has_next():
                context.update({"next_page": str(paginator.get_page(page.number + 1).object_list[0].pub_date)})
            if page.has_previous():
                context.update({"previous_page": str(paginator.get_page(page.number - 1).object_list[0].pub_date)})
    return render(request, template, context)
