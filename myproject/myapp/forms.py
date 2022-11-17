
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')



class PostForm(forms.ModelForm):
    # title = forms.CharField()
    # description = forms.CharField()
    # date=forms.DateField()
    # attachment = forms.FileField()

    class Meta:
        model = Post
        fields ="__all__"
