from django.urls import path
from . import views

urlpatterns = [
    path('new/' , views.create_book, name='create_book')
]