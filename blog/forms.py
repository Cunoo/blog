from django import forms

from .models import BlogPost, BlogEntry


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # include only text field
        fields = ['text']  # include only text field
        labels = {'text': ''}  # not generate a label for the text field


class EntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['textentry']
        labels = {'textentry': ''}
        widgets = {'textentry': forms.Textarea(attrs={'cols': 80})}  # text box with 80 columns wide


