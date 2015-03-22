# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('message', models.CharField(null=True, max_length=100, blank=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='author', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
