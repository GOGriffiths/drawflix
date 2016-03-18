import datetime
from django.db import models
from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify  -- Dont need?

class Drawing(models.Model):

    user = models.ForeignKey(User,blank=True, null=True)

    film = models.CharField(max_length=200) # name of film drawn
    image = models.CharField(max_length=655360,unique=True) # darwing, stored as base64string
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if self.likes < 0:
            self.likes = 0
        super(Drawing, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.film + str(self.id)
