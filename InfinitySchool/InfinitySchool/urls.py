from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from school.views import login, register, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)