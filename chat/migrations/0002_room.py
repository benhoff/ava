# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 3, 22, 19, 20, 58, 249777))),
                ('comment', models.TextField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
