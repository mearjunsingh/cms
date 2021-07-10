from django import forms
from .models import Comment


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-sm me-2'}), required=False, strip=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']