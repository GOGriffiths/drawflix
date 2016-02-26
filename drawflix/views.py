from django.shortcuts import render
from drawflix.models import Film, Drawing
from drawflix.forms import DrawingForm

import datetime
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    film_list = Film.objects.order_by('-title')[:5]
    context_dict = {'films': film_list}

    return render(request, 'drawflix/index.html', context_dict)

def add_drawing(request, title_in):

    try:
        target_film = Film.objects.get(title=title_in)
    except Film.DoesNotExist:
            target_film = None # this tabbing could be an issue

    if request.method == 'POST':
        form = DrawingForm(request.POST)

        if form.is_valid():
            if target_film:
                drawing = form.save(commit=False)
                drawing.film = target_film
                drawing.views = 0
                drawing.likes = 0
                drawing.save()
                return (request, title_in)

            # save form to databse
            # form.save(commit=True)

            # shows user the index page
            # TODO show user their drawing after sbmission
            # return index(request)

        else:
            print form.errors

    else:
        form = DrawingForm()

    context_dict = {'form': form, 'film': target_film}

    # TODO do we want to return this?
    # TODO return to page with text "drawing submitted"
    return render(request, 'drawflix/add_drawing.html', context_dict)

def about(request):

    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'drawflix/about.html', context_dict)

def most_recent(request):
    recent_drawings = Drawing.objects.order_by('-date')[:15]
    context_dict = {'recent_drawings': recent_drawings}
    return render(request, 'drawflix/most_recent.html', context_dict)

def trending(request):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days = 7)
    trending_drawings = Drawing.objects.filter(date__range=[start_date, end_date]).order_by('-likes')[:25]
    context_dict = {'trending_drawings': trending_drawings}
    return render(request, 'drawflix/trending.html', context_dict)

def hall_of_fame(request):
    recent_drawings = Drawing.objects.order_by('-date')[:15]
    context_dict = {'recent_drawings': recent_drawings}
    return render(request, 'drawflix/hall_of_fame.html', context_dict)


# def search(request):
#   context_dict
    # return render(request,'drawflix/search.html', context_dict)
