from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

from .models import Profile
from .forms import ProfileForm  # Assume you create a ProfileForm

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})