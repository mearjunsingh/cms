from django.urls import path
from .views import (
    HomePage
)


urlpatterns = [
    path('', HomePage.as_view(), name='homepage')
]