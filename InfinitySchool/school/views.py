import ast
import subprocess
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from school.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def code_checker(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        code = request.POST.get('code')
        result_message = ""

        practice_task = PracticeTasks.objects.filter(description=code).first()

        if practice_task:
            expected_answer = practice_task.answer.strip()

            if language == 'python':
                try:
                    ast.parse(code)
                    # Компиляция и выполнение кода с захватом вывода
                    process = subprocess.Popen(['python3', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    output = stdout.decode('utf-8').strip()  # Получение вывода программы

                    # Сравнение вывода с ожидаемым ответом
                    if output == expected_answer:
                        result_message = f'Ваш ответ: {output}\nЗадача решена! Поздравляем! 🎉'
                    else:
                        result_message = f'Ваш ответ: {output}\nК сожалению, это неправильно.\nНе отчаивайтесь! Попробуйте еще раз.'

                    
                except SyntaxError as e:
                    result_message = f"Ошибка синтаксиса Python: {str(e)}"

        response_data = {
            'message': result_message
        }
        
        return JsonResponse(response_data)

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
