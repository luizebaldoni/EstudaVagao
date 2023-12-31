'''ARQUIVO PARA DEFINIR AS ROTAS DA APLICAÇÃO '''

from django.urls import path, include
from django.contrib import admin
from .views import (
    home, detail, posts, create_post, latest_posts,
    search_result,)

# ORGANIZANDO ROTAS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("register.urls")),
    path("home", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("posts/<slug>/", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    path("latest_posts", latest_posts, name="latest_posts"),
    path("search", search_result, name="search_result"),
]

# CUSTOMIZAÇÃO DA ADMIN PAGE

admin.site.site_title = "Estuda Vagão admin (DEV)"
admin.site.site_header = "Administração Estuda Vagão"
admin.site.index_title = "Administração do Site"