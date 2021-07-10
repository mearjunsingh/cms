from posts.models import Post
from .models import Menu, Ad
from ..site_config import site_data


def site_config(request):
    return site_data


def menu_items(request):
    items = Menu.objects.all()
    return {'menu_items' : items}


def ad_items(request):
    ads = Ad.objects.filter(is_active=True)
    data = {}
    for ad in ads:
        data[ad.target] = ad.code
    return data


def sidebar_items(request):
    posts = Post.objects.filter(is_published=True)
    popular_posts = posts.order_by('-views')[:7]
    recent_posts = posts.order_by('-modified_date')[:7]
    context = {
        'popular_posts' : popular_posts,
        'recent_posts' : recent_posts
    }
    return context