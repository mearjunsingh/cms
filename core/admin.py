from django.contrib import admin
from .models import (
    MainMenu,
    TopMenu,
    FooterMenu,
    Page,
    Ad
)


admin.site.register(MainMenu)
admin.site.register(TopMenu)
admin.site.register(FooterMenu)
admin.site.register(Page)
admin.site.register(Ad)