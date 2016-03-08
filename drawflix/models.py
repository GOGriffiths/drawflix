import datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)


    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

# class Film(models.Model):
#     title = models.CharField(max_length=128, unique=True)
#     slug = models.SlugField()
#      #will it have a poster too?
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Film, self).save(*args, **kwargs)
#
#     def __unicode__(self):
#         return self.title

class Drawing(models.Model):

    film = models.CharField(max_length=200)
    # user = models.ForeignKey(User)

    # image = models.URLField()
    #!!!!!  replace this with the image url link
    image = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.image

class Like(models.Model):
    user = models.ForeignKey(User)
    drawing = models.ForeignKey(Drawing)
    # date or just like (how do we implement a like?)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        # not sure about this one
        return self.drawing
