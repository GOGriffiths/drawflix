# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0002_auto_20160225_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=models.SlugField(default=datetime.date(2016, 2, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='drawing',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
