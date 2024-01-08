# Generated by Django 4.2.7 on 2024-01-06 03:09

from django.db import migrations, models
import django_resized.forms
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=tinymce.models.HTMLField(verbose_name='Bibliografia'),
        ),
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(blank=True, max_length=40, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='author',
            name='points',
            field=models.IntegerField(default=0, verbose_name='Pontuação'),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[50, 80], upload_to='authors', verbose_name='Foto de perfil'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Sua pergunta'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=400, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('1', 'Matemática'), ('2', 'Física'), ('3', 'Química')], default=0, max_length=1, verbose_name='Disciplinas'),
            preserve_default=False,
        ),
    ]