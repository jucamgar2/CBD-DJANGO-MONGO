from django import forms
from .models import MongoUser

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    image = forms.ImageField(label='Imagen de perfil', required=False)

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("La imagen no puede pesar más de 2MB.")
            if image.content_type != 'image/jpeg':
                raise forms.ValidationError("La imagen debe ser de tipo JPEG.")
        return image

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3 or len(username) > 100:
            raise forms.ValidationError("El nombre de usuario debe tener entre 3 y 100 caracteres.")
        if MongoUser.objects.filter(username=username):
            raise forms.ValidationError("Ya existe un usuario con este nombre de usuario.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if MongoUser.objects.filter(email=email):
            raise forms.ValidationError("Ya existe un usuario con este correo.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4 or len(password) > 25:
            raise forms.ValidationError("La contraseña debe tener entre 4 y 25 caracteres.")
        return password

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)