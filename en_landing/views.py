from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import escapejs
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.views.generic import View

from core.models import Career, BlogPost

################################# BASE START ###################################

class IndexView(View):
    template = "en/base/index.html"
    def get(self, request):
        return render(request, self.template)

class AboutView(View):
    template = "en/base/about.html"
    def get(self, request):
        return render(request, self.template)

class ContactView(View):
    template = "en/base/contact.html"
    def get(self, request):
        return render(request, self.template)

class WorksView(View):
    template = "en/base/works.html"
    def get(self, request):
        return render(request, self.template)

################################# BASE END ###################################

################################# HIRING START ###################################

class HiringListView(View):
    template = "en/hiring/list.html"
    def get(self, request):
        careers = Career.objects.all()
        context = {
            'careers': careers
        }
        return render(request, self.template)

class HiringDetailsView(View):
    template = "en/hiring/details.html"
    def get(self, request):
        return render(request, self.template)

################################# HIRING END ###################################


################################# BLOG START ###################################
class BlogListView(View):
    template = "en/blog/list.html"
    def get(self, request):
        articles = BlogPost.objects.all()
        context = {
            'articles': articles
        }
        return render(request, self.template, context)

class BlogDetailsView(View):
    template = "en/blog/details.html"
    def get(self, request, *args, **kwargs):
        article_slug = kwargs.get('article')
        context = {
            'article': get_object_or_404(BlogPost, slug=article_slug)
        }
        return render(request, self.template, context)
################################# BLOG END ###################################


################################# SERVICES START ###################################

class ServicesView(View):
    template = "en/services/index.html"
    def get(self, request):
        return render(request, self.template)

################################# SERVICES END ###################################


def error_400(request,  exception):
    data = {}
    return render(request,'en/errors/400.html', data)

def error_403(request,  exception):
    data = {}
    return render(request,'en/errors/403.html', data)

def error_404(request, exception):
    data = {}
    return render(request,'en/errors/404.html', data)

def error_500(request):
    data = {}
    return render(request,'en/errors/500.html', data)
