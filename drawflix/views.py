from django.shortcuts import render
from drawflix.models import Film

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
