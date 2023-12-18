# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from blog.views import home, user_login, user_register, user_profile


app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('profile/', user_profile, name='profile'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), 
]
