from .models import MongoUser
from django.contrib.auth import login
from .models import MongoUser
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.files import File
from reservations.models import Reservation
from books.models import Book
from django.utils import timezone

import base64

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = MongoUser(username=username, email=email, password=make_password(password))
            if 'image' in request.FILES:
                image = request.FILES['image']
                user.image.put(image, content_type=image.content_type, filename=image.name)
            user.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = MongoUser.objects.filter(username=username).first()
            if user is not None and check_password(password, user.password):
                request.session['user_id'] = str(user.id)
                request.session['username'] = str(user.username)
                request.session['is_admin'] = user.is_admin
                return redirect('/')  
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['username']
        del request.session['is_admin']
    return redirect('/')

def new_admin(request):
    if 'is_admin' not in request.session:
        messages.warning(request, "Debe iniciar sesión como administrador para acceder a esta página.")
        return redirect('/login')
    if request.session['is_admin'] == False:
        messages.warning(request, "Solo los administradores pueden crear nuevos admin.")
        return redirect('/')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = MongoUser(username=username, email=email, password=make_password(password), is_admin=True)
            user.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'admin_register.html', {'form': form})

def get_user(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.warning(request, "Debe iniciar sesión para acceder a esta página.")
        return redirect('/login')
    user = MongoUser.objects.filter(id=user_id).first()
    image = user['image']
    if not image:
        with open('./users/static/images/book.png', 'rb') as image_file:
            image_b64 = base64.b64encode(image_file.read()).decode('utf-8')
    else:
        image_b64 = base64.b64encode(image.read()).decode('utf-8')
    reservations = Reservation.objects.filter(user=user, end_date__gte=timezone.now().date()).order_by('end_date')
    return render(request, 'profiles.html', {'user': user, 'image': image_b64, 'reservations': reservations})
