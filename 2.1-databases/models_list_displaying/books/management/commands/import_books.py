import json
from django.core.management import BaseCommand

from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("fixtures/books.json", encoding="utf-8") as f:
            books = json.load(f)
        for book in books:
            Book.objects.create(
                id=book.get("pk"),
                name=book.get("fields").get("name"),
                author=book.get("fields").get("author"),
                pub_date=book.get("fields").get("pub_date"),
            )
