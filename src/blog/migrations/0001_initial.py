# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0008_project_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(related_name='posts', to='projects.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
