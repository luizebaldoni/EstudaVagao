"""
NAO ALTERAR NADA NESTE ARQUIVO! PERMANECER COMO ESTA
ROTAS DEVEM SER ALTERADAS NO ARQUIVO URLS.PY NO DIRETORIO DJANGO_APP
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
	path('django_app/', include('django_app.urls')),
]