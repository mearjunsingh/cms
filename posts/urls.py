from django.urls import path
from core.views import HomePage
from .views import (
    PostDetail,
    CategoryList,
    TagList,
    AuthorList
)


urlpatterns = [
    path('browse/', HomePage.as_view()),
    path('article/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('category/<str:cat>/', CategoryList.as_view(), name='category_list'),
    path('tag/<str:tag>/', TagList.as_view(), name='tag_list'),
    path('author/<str:auth>/', AuthorList.as_view(), name='author_list'),
]