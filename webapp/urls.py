from django.conf.urls import patterns, url
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    #API
    url(r'^API/getreports/$', views.getreports, name='getreports'),

)