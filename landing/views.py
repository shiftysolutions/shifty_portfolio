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
    template = "fr/base/index.html"
    def get(self, request):
        return render(request, self.template)

class AboutView(View):
    template = "fr/base/about.html"
    def get(self, request):
        return render(request, self.template)

class ContactView(View):
    template = "fr/base/contact.html"
    def get(self, request):
        return render(request, self.template)

class WorksView(View):
    template = "fr/base/works.html"
    def get(self, request):
        return render(request, self.template)

################################# BASE END ###################################

################################# HIRING START ###################################

class HiringListView(View):
    template = "fr/hiring/list.html"
    def get(self, request):
        careers = Career.objects.all()
        context = {
            'careers': careers
        }
        return render(request, self.template)

class HiringDetailsView(View):
    template = "fr/hiring/details.html"
    def get(self, request):
        return render(request, self.template)

################################# HIRING END ###################################


################################# BLOG START ###################################
class BlogListView(View):
    template = "fr/blog/list.html"
    def get(self, request):
        posts = BlogPost.objects.all()
        context = {
            'posts': posts
        }
        return render(request, self.template)

class BlogDetailsView(View):
    template = "fr/blog/details.html"
    def get(self, request):
        return render(request, self.template)
################################# BLOG END ###################################


################################# SERVICES START ###################################

class ServicesView(View):
    template = "fr/services/index.html"
    def get(self, request):
        return render(request, self.template)

################################# SERVICES END ###################################
