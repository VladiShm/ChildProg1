from django.shortcuts import render


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'InfinitySchool/login.html', context)

def register(request):
    context = {
        'title': 'Register',
    }
    return render(request, 'InfinitySchool/register.html', context)

def index(request):
    context = {
        'title': 'InfinityCode',
    }
    return render(request, 'InfinitySchool/main_page.html', context)