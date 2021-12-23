from django import forms
from django.forms import widgets

from .models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model =Book
        fields= ['title','author','summary','isbn']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.TextInput(attrs={'class':'form-control'}),
            'isbn':forms.NumberInput(attrs={'class':'form-control'}),
        }