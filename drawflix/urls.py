from django.conf.urls import patterns, url
from drawflix import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
