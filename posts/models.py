from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from core.utils import upload_image_path, generate_unique_slug

User = get_user_model()

class Post(models.Model):
    title = models.CharField(_('Post Title'), max_length=150)
    excerpt = models.TextField(_('Post Excerpt'), max_length=300)
    thumbnail = models.ImageField(_('Post Thumbnail'), upload_to=upload_image_path, blank=True)
    slug = models.SlugField(_('Post Slug'), unique=True)
    content = RichTextUploadingField(_('Post Content'))
    categories = models.ManyToManyField('Category', verbose_name=_('Categories'), blank=True)
    tags = models.ManyToManyField('Tag', verbose_name=_('Tags'), blank=True)
    views = models.IntegerField(_('Post Views'), default=0, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, verbose_name=_('Post Author'))
    is_published = models.BooleanField(_('Is Published'), default=True)
    is_featured = models.BooleanField(_('Is Featured'), default=False)
    action_ip = models.CharField(_('Posted IP'), max_length=20, editable=False)
    modified_date = models.DateTimeField(_('Post Modified At'), auto_now=True)
    created_date = models.DateTimeField(_('Post Created At'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def get_absolute_url(self):
        return reverse_lazy('post_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_unique_slug(Post, self.title)
        return super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    display = models.CharField(_('Category'), max_length=100)
    slug = models.SlugField(_('Slug'), unique=True)

    def __str__(self):
        return self.display
    
    @property
    def get_absolute_url(self):
        return reverse_lazy('category_list', args=[self.slug])

    class Meta:
        verbose_name_plural = _('Categories')


class Tag(models.Model):
    display = models.CharField(_('Tag'), max_length=50)
    slug = models.SlugField(_('Slug'), unique=True)

    def __str__(self):
        return self.display
    
    @property
    def get_absolute_url(self):
        return reverse_lazy('tag_list', args=[self.slug])


class Comment(models.Model):
    body = RichTextUploadingField(_('Comment Body'), config_name='comment')
    is_approved = models.BooleanField(_('Is Approved'), default=False)
    created_date = models.DateTimeField(_('Comment Created On'), auto_now_add=True)
    action_ip = models.CharField(_('Comment Posted IP'), max_length=20, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Post'))

    def __str__(self):
        return self.user.display_name
