# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0004_auto_20160226_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='date',
        ),
        migrations.RemoveField(
            model_name='like',
            name='date',
        ),
    ]
