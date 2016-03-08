# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0009_auto_20160304_1039'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Film',
        ),
        migrations.AddField(
            model_name='drawing',
            name='film',
            field=models.CharField(default=b'', unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
