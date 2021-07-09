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

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.action_ip = get_client_ip(request)
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)