'''
Created on 24 nov. 2016

@author: teanocrata
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]