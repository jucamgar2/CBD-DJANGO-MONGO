from django import forms
from .models import Book
from .models import Genre

class BookForm(forms.Form):
    isbn = forms.CharField(label='ISBN')
    title = forms.CharField(label='Título')
    author = forms.CharField(label='Autor')
    year = forms.IntegerField(label='Año')
    description = forms.CharField(label='Descripción')
    genre = forms.ChoiceField(label='Género', choices=[(genre.name, genre.value) for genre in Genre])
    pages = forms.IntegerField(label='Páginas')
    language = forms.CharField(label='Idioma')
    show = forms.BooleanField(label='¿Mostrar?')
    image_link = forms.CharField(label='Enlace de imagen')
    
    def clean_genre(self):
        genre = self.cleaned_data['genre']
        genres = ['Ficción', 'Ciencia ficción', 'Drama', 'Misterio', 'Romance', 'Aventuras', 'Terror','Humor','Poesía','Cuento','Educativo','No ficción', 'Crimen']
        if genre not in genres:
            raise forms.ValidationError("El género no es válido.")
        return genre

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        if len(isbn) != 13:
            raise forms.ValidationError("El ISBN debe tener 13 caracteres.")
        if Book.objects.filter(isbn=isbn):
            raise forms.ValidationError("Ya existe un libro con este ISBN.")
        return isbn

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3 or len(title) > 100:
            raise forms.ValidationError("El título debe tener entre 3 y 100 caracteres.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 3 or len(author) > 100:
            raise forms.ValidationError("El autor debe tener entre 3 y 100 caracteres.")
        return author

    def clean_year(self):
        year = self.cleaned_data['year']
        if year < 1000 or year > 2024:
            raise forms.ValidationError("El año debe estar entre 1000 y 2024.")
        return year
    
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 50 or len(description) > 1500:
            raise forms.ValidationError("La descripción debe tener entre 50 y 1500 caracteres.")
        return description
    
    def clean_pages(self):
        pages = self.cleaned_data['pages']
        if pages < 1:
            raise forms.ValidationError("El número de páginas debe ser mayor a 0.")
        return pages
    
    def clean_language(self):
        language = self.cleaned_data['language']
        if len(language) < 3 or len(language) > 50:
            raise forms.ValidationError("El idioma debe tener entre 3 y 50 caracteres.")
        return language
    
    def clean_image_link(self):
        image_link = self.cleaned_data['image_link']
        if len(image_link) < 3 or len(image_link) > 255:
            raise forms.ValidationError("El enlace de imagen debe tener entre 3 y 255 caracteres.")
        return image_link