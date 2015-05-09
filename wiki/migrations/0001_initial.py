# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(null=True, blank=True, related_name='content_type_set_forarticle', to='contenttypes.ContentType', verbose_name='content type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleRevision',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('revision_number', models.IntegerField(editable=False)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('locked', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='wiki.Article')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('previous_revision', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wiki.ArticleRevision')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='current_revision',
            field=models.OneToOneField(null=True, blank=True, related_name='current_set', to='wiki.ArticleRevision', verbose_name='current revision'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(related_name='owned_articles', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
