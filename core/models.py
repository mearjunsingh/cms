from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
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
        if self.text:
            return self.text
        return 'Menu Item'
    
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
    
    @property
    def get_text(self):
        if self.text:
            return self.text
        elif self.category:
            return self.category.display
        elif self.tag:
            return self.tag.display
        elif self.page:
            return self.page.title
        else:
            return 'Some Link'
    
    class Meta:
        abstract = True



class MainMenu(Menu):
    class Meta:
        verbose_name_plural = 'Main Menu Items'


class TopMenu(Menu):
    class Meta:
        verbose_name_plural = 'Top Menu Items'


class FooterMenu(Menu):
    class Meta:
        verbose_name_plural = 'Footer Menu Items'


class Page(models.Model):
    title = models.CharField(_('Page Title'), max_length=150)
    excerpt = models.TextField(_('Page Excerpt'), max_length=300)
    thumbnail = models.ImageField(_('Page Thumbnail'), upload_to=upload_image_path, blank=True)
    slug = models.SlugField(_('Page Slug'), unique=True)
    content = RichTextUploadingField(_('Page Content'))
    is_published = models.BooleanField(_('Is Published'), default=True)
    modified_date = models.DateTimeField(_('Page Modified At'), auto_now=True)
    created_date = models.DateTimeField(_('Page Created At'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def get_absolute_url(self):
        return reverse_lazy('static_page', args=[self.slug])


class Ad(models.Model):
    targets = (
        ('ads_side1', 'Sidebar Top'),
        ('ads_side2', 'Sidebar Between'),
        ('ads_side3', 'Sidebar Bottom'),
        ('ads_header', 'Header'),
        ('ads_footer', 'Footer'),
        ('ads_homepage', 'Homepage'),
        ('ads_belowThumbnail', 'Below Thumbnail'),
        ('ads_belowPost', 'Below Post'),
        ('ads_belowRelated', 'Below Related'),
        ('ads_betweenPosts', 'Between Posts (Per 5)'),
        ('ads_belowFirstSection', 'Below First Section (Homepage)'),
        ('ads_belowSecondSection', 'Below Second Section (Homepage)')
    )
    title = models.CharField(_('Title'), max_length=100)
    target = models.CharField(_('Ad Target'), max_length=50, unique=True, choices=targets)
    code = models.TextField(_('Ad Code'))
    is_active = models.BooleanField(_('Active'), default=True)

    def __str__(self):
        return self.title


class Homepage(models.Model):
    sections = (
        ('section_one', 'Section One'),
        ('section_two', 'Section Two'),
        ('section_three', 'Section Three')
    )
    section = models.CharField(_('Section'), max_length=50, unique=True, choices=sections)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))

    def __str__(self):
        return self.section
    
    @property
    def get_absolute_url(self):
        return self.category.get_absolute_url
    
    class Meta:
        verbose_name_plural = _('Homepage')