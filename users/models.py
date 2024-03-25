from mongoengine import Document, StringField, EmailField

# Create your models here.
class MongoUser(Document):
    username = StringField(required=True, min_length=3, max_length=50, unique=True)
    password = StringField(required=True, min_length=4, max_length=50)
    email = EmailField(required=True, unique=True, max_length=200)

    meta = {'collection': 'users'}
