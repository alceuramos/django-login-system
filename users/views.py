from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ('Error on login try again.'))
            redirect('login')
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged out'))
    return redirect('dashboard')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            print(user)
            login(request, user)
            messages.success(request, (f'Hey, {username}! Your registration was successful!!!'))
            return redirect('dashboard')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')