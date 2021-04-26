
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from src.apps.catalog.views import Home


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", Home.as_view(), name="catalog.home"),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
