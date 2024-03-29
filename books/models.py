from mongoengine import Document, StringField, IntField, BooleanField

# Create your models here.
class Book(Document):
    isbn = StringField(required=True, min_length=13, max_length=13, unique=True)
    title = StringField(required=True, min_length=3, max_length=100)
    author = StringField(required=True, min_length=3, max_length=100)
    year = IntField(required=True, min_value=1000, max_value=2024)
    description = StringField(required=True, min_length=50, max_length=1500)
    genre = StringField(choices=('Ficción', 'Ciencia ficción', 'Drama', 'Misterio', 'Romance', 'Aventuras', 'Terror','Humor','Poesía','Cuento','Educativo','No ficción', 'Crimen'))
    pages = IntField(required=True, min_value=1)
    language = StringField(required=True, min_length=3, max_length=50)
    show = BooleanField(default=True)
    image_link = StringField(required=True, min_length=3, max_length=255)
    
    meta = {'collection': 'books'}