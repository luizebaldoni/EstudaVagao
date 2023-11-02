"""djangoProject URL Configuration
 Arquivo para armazenar as rotas que serão utilizadas no projeto.
 Este arquivo armazenará as rotas do projeto em geral, é recomendável que cada aplicação
 do projeto possua um arquivo de rotas específico
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.cadastro, name='cadastrar_usuario')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)