from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from posts.models import Post
from .models import Page, Homepage


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(is_published=True)
        sections = Homepage.objects.all()
        for section in sections:
            context[section.section] = posts.filter(categories=section.category)[:5]
            context[f'{section.section}_cat'] = section.category
        context['featured_posts'] = posts.filter(is_featured=True)[:3]
        return context


class StaticPage(DetailView):
    template_name = 'page.html'
    queryset = Page.objects.filter(is_published=True)


# class ContactPage(Form):
#     template_name = 'page.html'
#     queryset = Page.objects.filter(is_published=True)