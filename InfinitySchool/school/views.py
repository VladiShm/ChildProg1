from django.shortcuts import render
from school.models import *


def index(request):
    context = {
        'title': 'InfinityCode',
        'courses': Courses.objects.all(),
    }
    return render(request, 'InfinitySchool/main_page.html', context)

