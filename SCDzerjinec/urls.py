from django.contrib import admin
from django.urls import path, include
from . import settings as setts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if setts.DEBUG:
    urlpatterns += static(setts.MEDIA_URL, document_root=setts.MEDIA_ROOT)
