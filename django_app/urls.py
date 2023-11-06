'''
ARQUIVO PARA DEFINIR AS ROTAS DA APLICAÇÃO

'''

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_app.views import register_user, Login, home

urlpatterns = [
    path('', Login, name='login'),
    path('register/', register_user, name='register'),
    path('home/', home, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)