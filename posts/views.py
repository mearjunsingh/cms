from django.db.models import F
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post


class PostDetail(DetailView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.queryset.filter(slug=self.kwargs.get('slug'))
        post.update(views=F('views') + 1)
        context['bk'] = 'titleeeeeeeee'
        return context
    

class BaseListView(ListView):
    template_name = 'post_list.html'
    allow_empty = False


class CategoryList(BaseListView):
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True).filter(categories__slug=self.kwargs.get('cat'))


class TagList(BaseListView):
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True).filter(tags__slug=self.kwargs.get('tag'))


class AuthorList(BaseListView):
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True).filter(author__username=self.kwargs.get('auth'))