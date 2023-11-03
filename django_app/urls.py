from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_app.views import index, MyLoginView

urlpatterns = [
    path('', index, name='index'),
    path('register/', MyLoginView.as_view(), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)