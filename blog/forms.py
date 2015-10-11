from django import forms
from . import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('author', 'text')
        labels = {'author': 'Name', 'text': 'Comment'}
        widgets = {
            'author': forms.TextInput(attrs={'required': ''}),
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 4,
                                          'required': ''}),
        }

