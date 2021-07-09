from django.shortcuts import render
from django.views.generic import TemplateView
from posts.models import Post


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.all()[:3]
        return context

