import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drawflix_project.settings')

import django
django.setup()

from drawflix.models import Drawing
from django.contrib.auth.models import User


def populate():
    # user1 = add_user('Dickbutt')
    # # user2 = add_user('Doukie')

    add_drawing(user=user1,
                film=Shrek,
                image=shrek,
                views = 99,
                likes= 0)

def add_drawing(user, film, image, views = 0, likes = 0):
    d = Drawing.objects.get_or_create(film=film, image=image)[0]
    d.user = user
    d.views = views
    d.likes = likes
    d.save()
    return d


    # Print out what we have added to the user.
    # for c in .objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))


# Start execution here!
if __name__ == '__main__':
    print "Starting Drawflix population script..."
    populate()
