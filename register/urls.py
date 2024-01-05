from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("", signin, name="signin"),
    path("update_profile/", update_profile, name="update"),
    path("logout/", logout, name="logout"),
]