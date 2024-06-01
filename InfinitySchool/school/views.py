from django.shortcuts import render
from school.models import *


def index(request):
    context = {
        'title': 'InfinityCode',
        'courses': Courses.objects.all()[:3],
    }
    return render(request, 'InfinitySchool/main_page.html', context)


def catalog(request):
    context = {
        'courses': Courses.objects.all()
    }
    return render(request, 'InfinitySchool/catalog.html', context)