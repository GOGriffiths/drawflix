import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drawflix_project')

import django.setup()

from drawflix.models import UserProfile, Film, Drawing, Rating


def populate():
    user = add_user('Dickbutt')
    user = add_user('Doukie')

    add_(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    frame_cat = add_cat("Other Frameworks")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in .objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_drawing(title):
    f = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_film(title):
    f = Film.objects.get_or_create(title=title)[0]
    return f

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
