'''
ARQUIVO PARA DEFINIR OS TEMPLATES DA APLICAÇAO E O QUE FAZEMOS COM ELES
'''

from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.http import HttpResponseRedirect


def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "Estuda Vagão | CMSM"
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        try: # TESTA SE O USER TEM AUTORIZAÇÃO PARA VER E RESPONDER PERGUNTAS
            author = Author.objects.get(user=request.user)
        except:
            messages.error(request, 'Você não tem autorização para acessar ou responder perguntas.')
            messages.error(request, 'Contate um dos administradores para obter autorização.')
            #return redirect("home")
            return redirect(request.META.get('HTTP_REFERER', 'home'))
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)


    context = {
        "post":post,
        "title": "EstudaVagao: "+post.title,
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "Estuda Vagão: Perguntas"
    }

    return render(request, "posts.html", context)


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            try: # TESTA SE O USER TEM AUTORIZAÇÃO PARA PUBLICAR
                author = Author.objects.get(user=request.user)
            except:
                messages.error(request, 'Você não tem autorização para enviar perguntas. Contate um dos administradores para obter autorização.')
                messages.error(request, form.errors)
                return redirect("create_post")
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            messages.success(request, 'Sua pergunta foi enviada com sucesso.')
            return redirect("create_post")
    context.update({
        "form": form,
        "title": "EstudaVagao: Crie uma nova pergunta"
    })
    return render(request, "create_post.html", context)

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts": posts,
        "títulos": "EstudaVagao: Ultimas 10 perguntas"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):

    return render(request, "search.html")