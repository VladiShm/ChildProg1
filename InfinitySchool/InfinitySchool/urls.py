from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from school.views import index

admin.site.site_header = "INFINITY CODE"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
