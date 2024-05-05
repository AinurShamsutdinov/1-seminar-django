from datetime import datetime
from typing import Any

from django import forms
from sem_app_2.models import Author as AuthorModel

class RandomForm(forms.Form):
    random = forms.ChoiceField(choices=[('dice', 'Dice'), ('random', 'Random generator'), ('coin', 'Toss coin')])
    amount = forms.IntegerField(min_value=1, max_value=64)


class AuthorForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=30)
    last_name = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField()
    biography = forms.CharField()
    birthday = forms.DateField(initial=datetime.today())


class ArticleForm(forms.Form):
    head = forms.CharField(max_length=200)
    content = forms.CharField()
    publish_date = forms.DateField(initial=datetime.today())
    authors = forms.ChoiceField(choices=AuthorModel.objects.all().values_list('id', 'full_name')) 
    category = forms.CharField(max_length=100)
    published = forms.BooleanField(required=False)
   

class CommentForm(forms.Form):
    comment = forms.CharField(min_length=1, max_length=1000)
