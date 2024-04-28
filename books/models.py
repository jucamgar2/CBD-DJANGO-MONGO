from enum import Enum
from mongoengine import Document, StringField, IntField, BooleanField, EnumField, URLField

# Create your models here.

class Genre(Enum):
    Poesía = 'Poesía'
    Romance = 'Romance'
    Fantástica = 'Fantástica'
    Ciencia_ficción = 'Ciencia ficción'
    Terror = 'Terror'
    No_ficción = 'No ficción'
    Aventuras = 'Aventuras'
    Crimen = 'Crimen'
    Ficción = 'Ficción'
    Educativo = 'Educativo'
    Cuento = 'Cuento'
    Drama = 'Drama'
    Misterio = 'Misterio'
    Humor = 'Humor'


class Book(Document):
    isbn = IntField(required=True, min_length=13, max_length=13, unique=True)
    title = StringField(required=True, min_length=3, max_length=100)
    author = StringField(required=True, min_length=3, max_length=100)
    year = IntField(required=True, min_value=1000, max_value=2024)
    description = StringField(required=True, min_length=50, max_length=1500)
    genre = EnumField(Genre, required=True)
    pages = IntField(required=True, min_value=1)
    language = StringField(required=True, min_length=3, max_length=50)
    show = BooleanField(default=True)
    image_link = URLField(required=True, min_length=3, max_length=255)
    
    meta = {'collection': 'books'}