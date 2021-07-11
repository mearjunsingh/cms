from django.contrib import admin
from core.utils import get_client_ip
from .models import (
    Post,
    Category,
    Tag,
    Comment
)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'modified_date', 'views', 'is_published']
    search_fields = ['title', 'excerpt']
    sortable_by = ['title', 'views']
    list_per_page = 50
    date_hierarchy = 'created_date'
    readonly_fields = ['created_date', 'modified_date', 'slug', 'action_ip', 'author', 'views']
    list_editable = ['is_published']
    list_filter = ['is_published', 'is_featured', 'categories', 'tags']
    filter_horizontal = ['categories', 'tags']
    fieldsets = (
        (None, {
            'fields': (
                ('is_published', 'is_featured'),
                'title', 
                'thumbnail',
                'excerpt',
                'content',
                'categories',
                'tags'
            )
        }),
        ('More', {
            'classes': ('collapse',),
            'fields': (
                'slug',
                'views',
                'author',
                'action_ip',
                'modified_date',
                'created_date'
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user
            obj.action_ip = get_client_ip(request)
        super().save_model(request, obj, form, change)


@admin.register(Category, Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['display']
    list_display = ['display', 'slug']
    sortable_by = ['display']
    list_per_page = 50
    prepopulated_fields = {"slug": ("display",)}
    view_on_site = False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['user', 'post']
    list_display = ['user', 'post', 'created_date', 'is_approved']
    sortable_by = ['user' 'post']
    list_per_page = 50
    list_filter = ['is_approved']
    readonly_fields = ['created_date', 'action_ip', 'user', 'post']
    fieldsets = (
        (None, {
            'fields': (
                'user',
                'post',
                'body', 
                'is_approved'
            )
        }),
        ('More', {
            'classes': ('collapse',),
            'fields': (
                'action_ip',
                'created_date'
            ),
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False