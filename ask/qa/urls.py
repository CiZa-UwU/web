from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popular/.*$', views.popular, name='popular'),    
    url(r'^new/.*$', views.test),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question, name='question'),    
]