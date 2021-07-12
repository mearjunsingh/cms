from django.urls import path
from .views import (
    HomePage,
    StaticPage
)


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('contact/', HomePage.as_view(), name='contact_page'),
    path('<str:slug>/', StaticPage.as_view(), name='static_page')
]