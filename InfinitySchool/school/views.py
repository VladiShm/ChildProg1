from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


def course_detail(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    return render(request, 'InfinitySchool/course_detail.html', {'course': course})

def theory_and_tasks(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    theories = CoursesTheory.objects.filter(course=course)
    return render(request, 'InfinitySchool/theory_and_tacks.html', {'course': course, 'theories': theories})


def run_code(request):
    if request.method == "POST":
        code = request.POST.get("code", "")
        output = execute_code(code)
        return HttpResponse(f"<pre>{output}</pre>")
    return render(request, 'InfinitySchool/code_sandbox.html')


def execute_code(code):
    try:
        exec_locals = {}
        exec(code, globals(), exec_locals)
        res = exec_locals.get("result")

    except Exception as e:
        return str(e)
