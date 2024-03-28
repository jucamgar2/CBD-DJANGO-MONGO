from django import forms
from .models import MongoUser

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', min_length=3, max_length=100)
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, min_length=4, max_length=25)

    def clean_username(self):
        username = self.cleaned_data['username']
        if MongoUser.objects.filter(username=username):
            raise forms.ValidationError("Ya existe un usuario con este nombre de usuario.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if MongoUser.objects.filter(email=email):
            raise forms.ValidationError("Ya existe un usuario con este correo.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)