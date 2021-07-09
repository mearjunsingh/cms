from .models import Menu
from posts.models import Post


def menu_items(request):
    items = Menu.objects.all()
    return {'menu_items' : items}


def ad_items(request):
    context = {
        'ads_side1' : 'xa ni',
        'ads_side2' : 'df',
        'ads_side3' : 'dfdf',
        'ads_header' : 'ddfd',
        'ads_footer' : 'dfdfd',
        'ads_homepage' : 'd',
        'ads_belowThumbnail' : 'd',
        'ads_belowPost' : 'd',
        'ads_belowRelated' : 'd',
    }
    return context


def sidebar_items(request):
    posts = Post.objects.filter(is_published=True)
    popular_posts = posts.order_by('-views')[:7]
    recent_posts = posts.order_by('-modified_date')[:7]
    context = {
        'popular_posts' : popular_posts,
        'recent_posts' : recent_posts
    }
    return context