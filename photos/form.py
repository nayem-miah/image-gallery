from django import forms
from django.forms import widgets
from . models import *


class EditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        labels = {
            'catagory': 'Category...',
            'description': '',
            'photo': '',
        }
        widgets = widgets = {

            'description': forms.Textarea(attrs={'class': 'form-control'}),


        }
