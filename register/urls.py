from django.conf.urls.static import static
from django.urls import path

from cmsm_PROJECT import settings
from .views import *

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("", signin, name="signin"),
    path("update_profile/", update_profile, name="update"),
    path("logout/", logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)