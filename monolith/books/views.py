from django.shortcuts import render
from .models import Book

def catalog(request):
    books = Book.objects.all()
    return render(request, 'books/catalog.html', {'books': books})