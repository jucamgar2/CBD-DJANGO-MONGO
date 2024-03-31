from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.shortcuts import redirect

# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            year = form.cleaned_data['year']
            description = form.cleaned_data['description']
            genre = form.cleaned_data['genre']
            pages = form.cleaned_data['pages']
            language = form.cleaned_data['language']
            show = form.cleaned_data['show']
            image_link = form.cleaned_data['image_link']
            book = Book(isbn=isbn, title=title, author=author, year=year, description=description, genre=genre, pages=pages, language=language, show=show, image_link=image_link)  
            book.save()
            return redirect('/')
    else:
        form = BookForm()    
    return render(request, 'newbook.html', {'form': form})