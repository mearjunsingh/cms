from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import gettext_lazy as _
from posts.models import (
    Category,
    Tag
)
from .utils import upload_image_path


class Menu(models.Model):
    text = models.CharField(_('Menu Text'), max_length=100, blank=True, help_text=_('Displayed in case of link menu'))
    link = models.CharField(_('Menu Link'), max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'), blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name=_('Tag'), blank=True, null=True)
    page = models.ForeignKey('Page', on_delete=models.CASCADE, verbose_name=_('Page'), blank=True, null=True)

    def __str__(self) -> str:
        return self.text
    
    @property
    def get_absolute_url(self):
        if self.link:
            return self.link
        elif self.category:
            return self.category.get_absolute_url
        elif self.tag:
            return self.tag.get_absolute_url
        elif self.page:
            return self.page.get_absolute_url
        else:
            return '#'
    
    class Meta:
        verbose_name_plural = 'Menu Items'


class Page(models.Model):
    title = models.CharField(_('Page Title'), max_length=150)
    excerpt = models.CharField(_('Page Excerpt'), max_length=300)
    thumbail = models.ImageField(_('Page Thumbnail'), upload_to=upload_image_path)
    slug = models.SlugField(_('Page Slug'), unique=True)
    content = models.TextField(_('Page Content'))
    is_published = models.BooleanField(_('Is Published'), default=True)
    modified_date = models.DateTimeField(_('Page Modified At'), auto_now=True)
    created_date = models.DateTimeField(_('Page Created At'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def get_absolute_url(self):
        return '#'


class Ad(models.Model):
    targets = (
        ('test', 'test')
    )
    title = models.CharField(_('Title'), max_length=100)
    target = models.CharField(_('Ad Target'), max_length=10)
    code = models.TextField(_('Ad Code'))
    is_active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return self.title


class Site(models.Model):
    titles = (
        ('test', 'test'),
    )
    title = models.CharField(_('Site Title'), max_length=150, choices=titles, unique=True)
    excerpt = models.TextField(_('Site Excerpt'))
    logo = models.ImageField(_('Site Logo'), upload_to=upload_image_path)
    favico = models.ImageField(_('Site Favico'), upload_to=upload_image_path)
    footer_text = models.CharField(_('Footer Text'), max_length=255)
    
    def __str__(self):
        return self.title