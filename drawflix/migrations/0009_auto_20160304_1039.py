# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0008_auto_20160304_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='film',
        ),
        migrations.RemoveField(
            model_name='drawing',
            name='user',
        ),
    ]
