'''
ARQUIVO PARA DEFINIR AS ROTAS DA APLICAÇÃO

'''

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_app.views import  *

urlpatterns = [
    path('', Login, name='login'),
    path('cadastro/', cadastro, name='cadastro')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)