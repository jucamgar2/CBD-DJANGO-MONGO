from django.shortcuts import render
from books.models import Book

def welcome(request):
    books = Book.objects.filter(show=True)
    return render(request, 'welcome.html', {'books': books})
