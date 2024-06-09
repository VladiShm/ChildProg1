from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from school.views import index, catalog, course_detail, theory_and_tasks, run_code, toggle_like

admin.site.site_header = "INFINITY CODE"
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('catalog/', catalog, name='catalog'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/theory_and_tasks/', theory_and_tasks, name='theory_and_tasks'),
    path('run_code/', run_code, name='run_code'),
    path('toggle-like/<int:course_id>/', toggle_like, name='toggle_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
