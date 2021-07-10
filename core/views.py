from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from posts.models import Post
from .models import Page


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.all()[:3]
        return context


class StaticPage(DetailView):
    template_name = 'page.html'
    queryset = Page.objects.filter(is_published=True)


# class ContactPage(Form):
#     template_name = 'page.html'
#     queryset = Page.objects.filter(is_published=True)