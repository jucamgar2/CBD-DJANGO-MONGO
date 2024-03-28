from mongoengine import Document, StringField, ReferenceField, DateField
from books.models import Book
from users.models import MongoUser

# Create your models here.
class Reservation(Document):
    book = ReferenceField(Book, required=True)
    user = ReferenceField(MongoUser, required=True)
    start_date = DateField(required=True)
    end_date = DateField(required=True)
    
    meta = {'collection': 'reservations'}