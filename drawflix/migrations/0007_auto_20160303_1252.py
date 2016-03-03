# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('drawflix', '0006_auto_20160226_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=datetime.date(2016, 3, 3), upload_to=b'profile_images', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(default=datetime.date(2016, 3, 3), blank=True),
            preserve_default=False,
        ),
    ]
