from django.conf.urls import url, include
from django.contrib import admin
from qa.views import question, ask, popular, index, signup, login_view

from . import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^popular/.*$', popular, name='popular'),    
    url(r'^question/(?P<num>\d+)/', question, name='question'),
    url(r'^ask/', ask, name='ask'),
    url(r'^answer/', question,name='answer'),
    url(r'^signup/', signup, name='signup'),
    url(r'^login/',login_view,name='login')
]