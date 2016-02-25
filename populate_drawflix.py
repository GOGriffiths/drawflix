import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drawflix_project.settings')

import django
django.setup()

from drawflix.models import UserProfile, Film, Drawing, Like


def populate():
    # add_user('Dickbutt')
    # add_user('Doukie')

    add_film('Kill Bill')
    add_film('Die Hard')

    add_drawing('Kill Bill', 'Dickbutt', 'http://www.imdb.com/title/tt0266697/', 4, 0)
    add_drawing('Die Hard', 'Doukie', 'http://www.imdb.com/title/tt0095016/?ref_=fn_al_tt_1', 19, 12)

    add_rating('Dickbutt', 'http://www.imdb.com/title/tt0266697/')
    add_rating('Doukie', 'http://www.imdb.com/title/tt0095016/?ref_=fn_al_tt_1')

    # Print out what we have added to the user.
    # for c in .objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))

def add_user(user):
    u = Like.objects.get_or_create(user=user)[0]
    username = user
    u.save()
    return u

def add_like(user, drawing, date):
    r = Like.objects.get_or_create(user=user, drawing=drawing)[0]
    r.date = date
    r.save()
    return r

def add_drawing(film, user, image, views, likes, date):
    d = Drawing.objects.get_or_create(film=film, image=image)[0]
    d.user = user
    d.views = views
    d.likes = likes
    d.date = date
    d.save()
    return d

def add_film(title):
    f = Film.objects.get_or_create(title=title)[0]
    f.save()
    return f

# Start execution here!
if __name__ == '__main__':
    print "Starting Drawflix population script..."
    populate()
