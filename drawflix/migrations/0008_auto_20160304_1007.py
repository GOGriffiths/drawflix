# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0007_auto_20160303_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='image',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
