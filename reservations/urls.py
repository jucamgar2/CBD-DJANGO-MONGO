from django.urls import path
from . import views

urlpatterns = [
    path('reservate/<str:id>', views.reservate, name='reservate'),
]