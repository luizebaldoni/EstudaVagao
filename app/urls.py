'''ARQUIVO PARA DEFINIR AS ROTAS DA APLICAÇÃO '''

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app.views import *

# ORGANIZANDO ROTAS
urlpatterns = [
    # path('', , name=''), # pagina inicial / login

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # define que possui elementos estaticos no view