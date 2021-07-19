from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="With country code")

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows' : 5}),
        }
