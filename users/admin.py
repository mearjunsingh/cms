from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ['-date_joined']
    list_display = ['username', 'email', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    add_fieldsets = (
        (None, {
            'fields' : (
                'username',
                'email',
                'password1',
                'password2'
            )
        }),
        ('Details', {
            'fields' : (
                ('first_name', 'last_name'),
                'bio',
                'url',
                'profile_photo'
            )
        }),
        ('Permissions', {
            'fields' : (
                'is_verified',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )
    fieldsets = (
        ('Meta', {
            'fields' : (
                'email', 
                'username',
                ('first_name', 'last_name'),
                'bio',
                'url',
                'profile_photo'
            )
        }),
        ('Details', {
            'fields': (
                'is_verified',
                'is_active',
                'is_staff',
                'is_superuser',
                'last_login',
                'date_joined'
                )
        }),
        ('Permissions', {
            'classes' : ('collapse',),
            'fields' : (
                ('groups'),
                ('user_permissions')
            )
        })
    )
    list_per_page = 50
    readonly_fields = ['last_login', 'date_joined']