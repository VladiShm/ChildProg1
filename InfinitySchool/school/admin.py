from django.contrib import admin
from school.models import Courses, CoursesTheory, PracticeTasks, Reviews

admin.site.register(Courses)

admin.site.register(CoursesTheory)

admin.site.register(PracticeTasks)

admin.site.register(Reviews)