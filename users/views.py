from .models import MongoUser
from django.contrib.auth import login
from .models import MongoUser
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = MongoUser(username=username, email=email, password=make_password(password))
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
                return redirect('/')  
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')