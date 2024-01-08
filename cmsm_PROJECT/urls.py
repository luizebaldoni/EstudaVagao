"""

NAO ALTERAR NADA NESTE ARQUIVO! PERMANECER COMO ESTA
ROTAS DEVEM SER ALTERADAS NO ARQUIVO URLS.PY NO DIRETORIO APP

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('register.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)