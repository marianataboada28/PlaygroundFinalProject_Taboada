# blog/views.py


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserForm, UserProfileForm
from .models import UserProfile

def home(request):
    return render(request, 'blog/home.html')

def user_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('blog:login')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'blog/register.html', {'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('blog:profile')

    return render(request, 'blog/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('blog:login')

@login_required
def user_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('blog:profile')

    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {'profile_form': profile_form})
