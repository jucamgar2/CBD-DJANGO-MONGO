from django.urls import path
from . import views

urlpatterns = [
    path('' , views.get_books, name='get_books'),
    path('new/' , views.create_book, name='create_book'),
    path('<str:id>/', views.get_book, name='get_book')
]