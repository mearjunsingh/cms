from django.db.models import F
from django.contrib.auth import get_user_model
User = get_user_model()
from django.views.generic import ListView, DetailView
from core.utils import get_client_ip
from .models import Category, Comment, Post, Tag
from .forms import CommentForm


class PostDetail(DetailView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.queryset.filter(slug=self.kwargs.get('slug'))
        post.update(views=F('views') + 1)
        context['related_posts'] = Post.objects.filter(is_published=True).filter(author=context['post'].author).exclude(id=context['post'].id).order_by('-modified_date')[:3]
        context['comment_form'] = CommentForm(None)
        if self.request.POST.get('body'):
            context['comment_msg'] = 'Your comment has been submitted and is being reviewed
.'
        context['comments'] = Comment.objects.filter(post=context['post']).filter(is_approved=True).order_by('-id')
        return context
    
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.action_ip = get_client_ip(self.request)
            comment.post = self.get_object(self.queryset)
            comment.save()
        return super().get(self, self.request, *args, **kwargs)
    

class BaseListView(ListView):
    template_name = 'post_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        b_url = '?'
        term = self.request.GET.get('search')
        if term:
            b_url += f'search={term}&'
            context['search_term'] = term
        context['base_url'] = b_url
        return context


class BrowseList(BaseListView):

    def get_queryset(self):
        posts = Post.objects.filter(is_published=True).order_by('-modified_date')
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts


class CategoryList(BaseListView):
    
    def get_queryset(self):
        posts = Post.objects.filter(is_published=True).filter(categories__slug=self.kwargs.get('cat')).order_by('-modified_date')
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_term'] = Category.objects.get(slug=self.kwargs.get("cat")).display
        context['list_type'] = 'category'
        return context


class TagList(BaseListView):
    
    def get_queryset(self):
        posts =  Post.objects.filter(is_published=True).filter(tags__slug=self.kwargs.get('tag')).order_by('-modified_date')
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_term'] = Tag.objects.get(slug=self.kwargs.get("tag")).display
        context['list_type'] = 'tag'
        return context


class AuthorList(BaseListView):
    
    def get_queryset(self):
        posts =  Post.objects.filter(is_published=True).filter(author__username=self.kwargs.get('auth')).order_by('-modified_date')
        term = self.request.GET.get('search')
        if term:
            posts = posts.filter(title__icontains=term)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_term'] = User.objects.get(username=self.kwargs.get("auth")).display_name
        context['list_type'] = 'author'
        return context
