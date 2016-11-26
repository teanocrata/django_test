'''
Created on 26 nov. 2016

@author: teanocrata
'''
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)