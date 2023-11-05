'''
ARQUIVO PARA DEFINIR AS ROTAS DA APLICAÇÃO

'''

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_app.views import index, register_user

urlpatterns = [
    path('login/', index.as_view(), name='login'),
    path('login/register/', register_user.as_view(), name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)