from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from school.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def code_checker(request):
    return render(request, 'InfinitySchool/task.html')

def index(request):
    context = {
        'title': 'InfinityCode',
        'courses': Courses.objects.all()[:3],
    }
    return render(request, 'InfinitySchool/main_page.html', context)


def catalog(request):
    courses = Courses.objects.all()
    liked_courses = []
    if request.user.is_authenticated:
        liked_courses = Like.objects.filter(user=request.user).values_list('course_id', flat=True)
    
    context = {
        'courses': courses,
        'liked_courses': liked_courses,
    }
    return render(request, 'InfinitySchool/catalog.html', context)

@login_required
def toggle_like(request, course_id):
    course = get_object_or_404(Courses, id=course_id)
    like, created = Like.objects.get_or_create(user=request.user, course=course)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked})

def course_detail(request, course_id):
    course = get_object_or_404(Courses, pk=course_id)
    theories = course.theories.all()
    if course.name != "Полный курс изучения Python":
        return render(request, 'InfinitySchool/course_in_development.html')

    theories = course.theories.all()
    return render(request, 'InfinitySchool/course_detail.html', {'course': course, 'theories': theories})




def execute_code(code):
    try:
        exec_locals = {}
        exec(code, globals(), exec_locals)
        res = exec_locals.get("result")

    except Exception as e:
        return str(e)
    
#def send_review(request):
#   return render(request, 'InfinitySchool/send_review.html')

@login_required
def send_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review')
        user = request.user

        # Создание нового отзыва
        Reviews.objects.create(user=user, rating=rating, review=review_text)

    return render(request, 'InfinitySchool/send_review.html')
