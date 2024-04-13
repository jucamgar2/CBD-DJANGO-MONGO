from django.shortcuts import render
from .forms import ReservationForm
from .models import Reservation
from books.models import Book
from django.shortcuts import redirect
from django.contrib import messages
from users.models import MongoUser


# Create your views here.
def reservate(request, id):
    if 'user_id' not in request.session:
        return redirect('/login')
    if request.method == 'POST':
        book = Book.objects.get(isbn=id)
        form = ReservationForm(request.POST, book = book)
        user = MongoUser.objects.get(id=request.session['user_id'])
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            reservation = Reservation(book=book, user=user, start_date=start_date, end_date=end_date)
            reservation.save()
            messages.success(request, "Reserva exitosa.")
            return redirect('/')
    else:
        book = Book.objects.get(isbn=id)
        form = ReservationForm()
    return render(request, 'reservate.html', {'book': book, 'form': form})   