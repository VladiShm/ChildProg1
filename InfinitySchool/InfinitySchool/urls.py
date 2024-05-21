from django.contrib import admin
from django.urls import path

from school.views import login, register, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
