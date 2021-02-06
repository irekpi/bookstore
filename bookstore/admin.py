from django.contrib import admin
from bookstore.models import Book, Author, BookAuthor, Publisher

admin.site.register(Book)
admin.site.register(Author)

admin.site.register(BookAuthor)
admin.site.register(Publisher)
