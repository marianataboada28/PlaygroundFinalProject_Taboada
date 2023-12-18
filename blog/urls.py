# blog/urls.py
from django.urls import path
from .views import home, user_register, user_login, user_logout, user_profile
from . import views

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='profile'),
    path('profile/', views.user_profile, name='profile'),
]


#