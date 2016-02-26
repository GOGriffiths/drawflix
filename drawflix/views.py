from django.shortcuts import render
from drawflix.models import Film, Drawing

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

def about(request):

    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'drawflix/about.html', context_dict)

def most_recent(request):
    recent_drawings = Drawing.objects.order_by('-date')[:15]
    context_dict = {'recent_drawings': recent_drawings}
    return render(request, 'drawflix/most_recent.html', context_dict)

def trending(request):
    end_date = datetime.date.today()
    start_date = timezone.now() - datetime.timedelta(days = 7)
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
