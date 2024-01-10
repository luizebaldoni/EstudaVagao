''' ARQUIVO PARA DEFINIR O LAYOUT DO BANCO DE DADOS '''
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField
from hitcount.models import HitCount
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

User = get_user_model()

# Class (teste) para alteração do register
'''
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, matricula, ano, password=None):
        
        if not email:
            raise ValueError("O usuário necessita de um email")
        if not username:
            raise ValueError("O usuário necessita de um username")
        if not matricula:
            raise ValueError("O usuário necessita de seu número de matrícula")
        if not ano:
            raise ValueError("O usuário necessita de seu ano escolar")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            matricula=matricula,
            ano=ano,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="endereço de email",
        max_length=255,
        unique=True,
    )
    username = models.TextField()
    matricula = models.IntegerField()
    ano = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "username", "matricula", "ano"]

    def __str__(self):
        return self.username
'''

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True, verbose_name=("Nome Completo"))
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = HTMLField(verbose_name=("Bibliografia"))
    points = models.IntegerField(default=0, verbose_name=("Pontuação"))
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True, blank=True, verbose_name=("Foto de perfil"))

    def __str__(self):
        return self.fullname

    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("posts", kwargs={
            "slug":self.slug
        })

    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")


class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:100]

DISCIPLINAS = (
        ("1", "Matemática"), 
        ("2", "Física"), 
        ("3", "Química"),
        ("4", "Biologia"),
        ("5", "História"),
        ("6", "Geografia"),
        ("7", "Filosofia"),
        ("8", "Sociologia"),
        ("9", "Português"),
        ("10", "Literatura"),
        ("11", "Inglês"),
        ("12", "Espanhol"),
        ("13", "Arte"),
        ("14", "Educação Física"),
        ("15", "Outra"),
    )

ANO = (
    ("1", "Fundamental: 6º ano"),
    ("2", "Fundamental: 7º ano"),
    ("3", "Fundamental: 8º ano"),
    ("4", "Fundamental: 9º ano"),
    ("5", "Ensino Médio: 1º ano"),
    ("6", "Ensino Médio: 2º ano"),
    ("7", "Ensino Médio: 3º ano"),
)    

class Post(models.Model):
    title = models.CharField(max_length=400, verbose_name='Título')
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Sua pergunta")
    #categories = models.CharField(max_length=400, choices=DISCIPLINAS, blank=False, null=False, verbose_name="Disciplinas") --> Essa categoria é criada via código
    categories = models.ManyToManyField(Category, verbose_name="Disciplina") # --> essa categoria (disciplina) é criada via admin
    ano_escolar = models.CharField(max_length=400, choices=ANO, blank=False, null=False, verbose_name="Ano Escolar")  #Adicionar de maneira igual a categories
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    tags = TaggableManager(verbose_name="tags")
    comments = models.ManyToManyField(Comment, blank=True)
    closed = models.BooleanField(default=False)
    state = models.CharField(max_length=40, default="zero")
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug
        })

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest("date")


