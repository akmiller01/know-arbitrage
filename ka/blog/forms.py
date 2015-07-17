from django import forms
from django.forms import ModelForm
from blog.models import Comment

class CommentForm(ModelForm):
    author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3}))
    class Meta:
        model = Comment
        exclude = ["post"]