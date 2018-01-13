from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from . import forms


class HomeView(TemplateView):
    template_name = "core_blog/index.html"


class CreatePost(CreateView):
    form_class = forms.CreatePostForm
    success_url = '/'
    template_name = 'core_blog/post_form.html'


class AboutView(TemplateView):
    template_name = 'core_blog/about.html'
