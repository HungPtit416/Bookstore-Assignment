from django.contrib import admin
from django.urls import path
from books.views import create_book, get_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', get_books),
    path('books/create/', create_book),
]
