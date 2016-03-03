from django.conf.urls import patterns, url
from drawflix import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^most_recent/$', views.most_recent, name='most_recent'),
        url(r'^trending/$', views.trending, name='trending'),
        url(r'^hall_of_fame/$', views.hall_of_fame, name='hall_of_fame'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        )
