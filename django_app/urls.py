from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'django_app'
urlpatterns = [
    path(' ', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)