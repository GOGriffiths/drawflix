# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0010_auto_20160308_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='film',
            field=models.CharField(max_length=200),
        ),
    ]
