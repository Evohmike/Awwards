from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']


class DesignForm(forms.ModelForm):
   class Meta:
       model = DesignRating
       fields = ['rating']

class UsabilityForm(forms.ModelForm):
   class Meta:
       model = UsabilityRating
       fields = ['rating']

class ContentForm(forms.ModelForm):
   class Meta:
       model = ContentRating
       fields = ['rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        fields = ['comment'] 
