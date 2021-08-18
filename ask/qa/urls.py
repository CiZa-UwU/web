from django.conf.urls import url, include
from django.contrib import admin
from qa.views import question, ask

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popular/.*$', views.popular, name='popular'),    
    url(r'^question/(?P<pk>\d+)/', question, name='question'),
    url(r'^ask/', ask, name='ask')
]