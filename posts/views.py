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
        context['related_posts'] = Post.objects.filter(is_published=True).filter(author=context['post'].author).exclude(id=context['post'].id).order_by('-modified_date')[:3]
        return context
    

class BaseListView(ListView):
    template_name = 'post_list.html'
    allow_empty = False
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        b_url = '?'
        term = self.request.GET.get('search')
        if term:
            b_url += f'search={term}&'
        context['base_url'] = b_url
        # context['search_form'] = PostFilterForm(self.request.GET or None)
        return context


class CategoryList(BaseListView):
    
    def get_queryset(self):
        posts = Post.objects.filter(is_published=True).filter(categories__slug=self.kwargs.get('cat'))
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Show Cate'
        return context


class TagList(BaseListView):
    
    def get_queryset(self):
        posts =  Post.objects.filter(is_published=True).filter(tags__slug=self.kwargs.get('tag'))
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Show tttaaagg'
        return context


class AuthorList(BaseListView):
    
    def get_queryset(self):
        posts =  Post.objects.filter(is_published=True).filter(author__username=self.kwargs.get('auth'))
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Show daaaaa'
        return context