from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from school.views import index, catalog

admin.site.site_header = "INFINITY CODE"
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('catalog/', catalog, name='catalog')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
