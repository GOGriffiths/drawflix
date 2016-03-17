import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Drawing(models.Model):

    film = models.CharField(max_length=200)
    user = models.ForeignKey(User,blank=True, null=True)
    image = models.CharField(max_length=65536,unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.image
