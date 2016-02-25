# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drawflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('drawing', models.ForeignKey(to='drawflix.Drawing')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rating',
            name='drawing',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.RemoveField(
            model_name='drawing',
            name='title',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='drawing',
            name='date',
            field=models.DateField(default=datetime.date(2016, 2, 25)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drawing',
            name='image',
            field=models.URLField(default=datetime.date(2016, 2, 25)),
            preserve_default=False,
        ),
    ]
