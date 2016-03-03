from django.shortcuts import render
from drawflix.models import Film, Drawing
from drawflix.forms import DrawingForm, UserForm, UserProfileForm
# from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.utils import timezone
# from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context_dict = {}
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits


    response = render(request,'drawflix/index.html', context_dict)

    return response

def about(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'drawflix/about.html', context_dict)

def most_recent(request):
    recent_drawings = Drawing.objects.order_by('-date')[:15]
    context_dict = {'recent_drawings': recent_drawings}
    return render(request, 'drawflix/most_recent.html', context_dict)

def trending(request):
    # end_date = datetime.date.today()
    # start_date = end_date - datetime.timedelta(days = 7)
    # trending_drawings = Drawing.objects.filter(date__range=[start_date, end_date]).order_by('-likes')[:25]
    # context_dict = {'trending_drawings': trending_drawings}
    return render(request, 'drawflix/trending.html')

def hall_of_fame(request):
    recent_drawings = Drawing.objects.order_by('-date')[:15]
    context_dict = {'recent_drawings': recent_drawings}
    return render(request, 'drawflix/hall_of_fame.html', context_dict)
