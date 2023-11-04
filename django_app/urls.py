from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_app.views import index, MyLoginView, RegisterView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('login/register/', RegisterView.as_view(), name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)