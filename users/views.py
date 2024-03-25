from django.shortcuts import render
from .models import MongoUser

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = MongoUser(username=username, email=email, password=password)
        user.save()
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')