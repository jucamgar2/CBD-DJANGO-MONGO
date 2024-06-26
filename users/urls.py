from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.get_user, name='profile'),
    path('users/admin/new/',views.new_admin, name='new_admin'),
]