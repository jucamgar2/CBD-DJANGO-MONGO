from .models import MongoUser
from django.contrib.auth import login
from .models import MongoUser
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    #if 'user_id' in request.session:
        #print(request.session['user_id'])
    print(request.session.get('user_id'))
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = MongoUser(username=username, email=email, password=password)
        user.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = MongoUser.objects(username=username, password=password).first()
        if user is not None:
            print('Valid login')
            print(user.id)
            request.session['user_id'] = str(user.id)
            return redirect('/register')
        else:
            print('Invalid login')
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')