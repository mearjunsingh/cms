from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
    PasswordResetForm,
    SetPasswordForm
)
from posts.models import Comment, Post, Category, Tag


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'), widget=forms.TextInput({'class' : 'form-control'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput({'class' : 'form-control'}))


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autofocus'] = False

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}), required=True)
    password1 = forms.CharField(label=_('Password'), help_text=_('Strong password required'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}), required=True)


class NewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('Password'), help_text=_('Strong password required'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    new_password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'thumbnail', 'categories', 'tags', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows' : 3}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PostFilterForm(forms.Form):
    PUBLISHED_CHOICES = [
        ('', 'All'),
        ('published', 'Published'),
        ('draft', 'Draft')
    ]
    term = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    category = forms.ModelChoiceField(required=False, queryset=Category.objects.all(), widget=forms.Select(attrs={'class' : 'form-select'}))
    tag = forms.ModelChoiceField(required=False, queryset=Tag.objects.all(), widget=forms.Select(attrs={'class' : 'form-select'}))
    status = forms.ChoiceField(required=False, choices=PUBLISHED_CHOICES, initial='', widget=forms.RadioSelect(attrs={'class' : 'form-check-input'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['is_approved']
    

class CommentFilterForm(forms.Form):
    COMMENT_CHOICES = [
        ('', 'All'),
        ('approved', 'Approved'),
        ('pending', 'Pending')
    ]
    term = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    status = forms.ChoiceField(required=False, choices=COMMENT_CHOICES, initial='', widget=forms.RadioSelect(attrs={'class' : 'form-check-input'}))


class ProfileForm(forms.ModelForm):
    form_classes = 'form-control'

    class Meta:
        model = User
        fields = ['profile_photo', 'username', 'email', 'first_name', 'last_name', 'bio', 'url']
        widgets = {
            'profile_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows' : 3}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput({'class' : 'form-control'}))
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput({'class' : 'form-control'}))
    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput({'class' : 'form-control'}))