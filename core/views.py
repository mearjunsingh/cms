from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from posts.models import Post
from .models import Contact, Page, Homepage
from .forms import ContactForm


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


class ContactPage(SuccessMessageMixin, CreateView):
    template_name = 'contact.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contact_page')
    success_message = "Message submitted successfully."


class StaticPage(DetailView):
    template_name = 'page.html'
    queryset = Page.objects.filter(is_published=True)
