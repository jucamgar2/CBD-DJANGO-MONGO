from mongoengine import Document, StringField, IntegerField, BooleanField

# Create your models here.
class Book(Document):
    isbn = StringField(required=True, min_length=13, max_length=13, unique=True)
    title = StringField(required=True, min_length=3, max_length=100)
    author = StringField(required=True, min_length=3, max_length=100)
    year = IntegerField(required=True, min_value=1000, max_value=2023)
    description = StringField(required=True, min_length=200, max_length=1000)
    genre = StringField(choices=('Ficción', 'Ciencia ficción', 'Drama', 'Misterio', 'Romance', 'Aventuras', 'Terror','Humor','Poesía','Cuento'))
    pages = IntegerField(required=True, min_value=1)
    language = StringField(required=True, min_length=3, max_length=50)
    show = BooleanField(default=True)
    
    meta = {'collection': 'books'}