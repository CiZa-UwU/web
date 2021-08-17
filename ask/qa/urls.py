from django.conf.urls import url, include
from django.contrib import admin
from qa.views import question

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popular/.*$', views.popular, name='popular'),    
    url(r'^question/(?P<num>\d+)/', question, name='question'),
    url(r'^ask/', views.ask, name='ask')
]