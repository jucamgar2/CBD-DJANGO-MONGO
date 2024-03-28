import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CBD.settings')
django.setup()

from mongoengine import connect
from mongoengine.errors import NotUniqueError
from users.models import MongoUser
from django.contrib.auth.hashers import make_password

def create_admin_user():
    print("Creating admin user...")
    connect('cbd')
    if not MongoUser.objects(is_admin=True).first():
        try:
            MongoUser(
                username='admin',
                password=make_password('4dm1n'),
                email='admin@admin.com',
                is_active=True,
                is_admin=True
            ).save()
            print("Admin user created.")
        except NotUniqueError:
            print("Admin user already exists.")
    else:
        print("An admin user already exists.")

if __name__ == '__main__':
    create_admin_user()