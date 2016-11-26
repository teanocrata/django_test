'''
Created on 24 nov. 2016

@author: teanocrata
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='blog.views.post_detail'),
    url(r'^post/new/$', views.post_new, name='blog.views.post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='blog.views.post_edit'),
]