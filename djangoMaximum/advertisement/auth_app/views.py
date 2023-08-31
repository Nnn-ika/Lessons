from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            return render(request, 'auth_app/register.html', {'error' : 'Ошибка! Проверьте корректно ли заполнена форма.'})
    else:
        form = RegistrationForm()
    context = {'form' : form}
    return render(request, 'auth_app/register.html', context)

def logIn(request):
    if request.method == 'GET':
        return render(request, 'auth_app/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('profile'))
        else:
            return render(request, 'auth_app/login.html', {'error' : 'Пользователь не найден.'})

def profile(request):
    return render(request, 'auth_app/profile.html')

@login_required(login_url=reverse_lazy('login'))
def profileView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return profile(request)
        else:
            return redirect(reverse('login'))
    
@login_required(login_url=reverse_lazy('login'))
def logOut(request):
    logout(request)
    return redirect(reverse('login'))