from django.shortcuts import render
from .forms import BookForm

# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()    
    return render(request, 'newbook.html', {'form': form})