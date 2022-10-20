from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
