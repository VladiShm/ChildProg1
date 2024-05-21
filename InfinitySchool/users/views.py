from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm
from django.urls import reverse
from django import forms


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Login',
        'form': UserLoginForm()
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'Register',
    }
    return render(request, 'users/register.html', context)
