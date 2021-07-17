from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import (
    MainMenu,
    TopMenu,
    FooterMenu,
    Page,
    Ad,
    Homepage
)

@admin.register(MainMenu, TopMenu, FooterMenu)
class MenuAdmin(ModelAdmin):
    list_display = ['get_text', 'get_absolute_url']
    search_fields = ['text', 'get_text']
    sortable_by = ['text']
    list_per_page = 50
    view_on_site = False
    autocomplete_fields = ['category', 'tag', 'page']


@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'modified_date', 'is_published']
    search_fields = ['title', 'excerpt']
    sortable_by = ['title']
    list_per_page = 50
    date_hierarchy = 'created_date'
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['created_date', 'modified_date']
    list_editable = ['is_published']
    list_filter = ['is_published']
    fieldsets = (
        (None, {
            'fields': (
                ('title', 'slug'),
                'thumbnail',
                'excerpt',
                'content'
            )
        }),
        ('More', {
            'classes': ('collapse',),
            'fields': (
                'is_published',
                'modified_date',
                'created_date'
            ),
        }),
    )


@admin.register(Ad)
class AdAdmin(ModelAdmin):
    list_display = ['title', 'target', 'is_active']
    search_fields = ['title', 'target']
    sortable_by = ['title', 'target']
    list_editable = ['is_active']
    list_per_page = 50
    list_filter = ['is_active']


@admin.register(Homepage)
class HomepageAdmin(ModelAdmin):
    list_display = ['section', 'category']
    autocomplete_fields = ['category']
    view_on_site = False