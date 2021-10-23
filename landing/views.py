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
    template = "index.html"
    def get(self, request):
        return render(request, self.template)

class AboutView(View):
    template = "about.html"
    def get(self, request):
        return render(request, self.template)

class ContactView(View):
    template = "contact.html"
    def get(self, request):
        return render(request, self.template)

class WorksView(View):
    template = "works/index.html"
    def get(self, request):
        return render(request, self.template)

################################# BASE END ###################################

################################# HIRING START ###################################

class HiringListView(View):
    template = "hiring/list.html"
    def get(self, request):
        careers = Career.objects.all()
        context = {
            'careers': careers
        }
        return render(request, self.template)

class HiringDetailsView(View):
    template = "hiring/details.html"
    def get(self, request):
        return render(request, self.template)

################################# HIRING END ###################################


################################# BLOG START ###################################
class BlogListView(View):
    template = "blog/list.html"
    def get(self, request):
        posts = BlogPost.objects.all()
        context = {
            'posts': posts
        }
        return render(request, self.template)

class BlogDetailsView(View):
    template = "blog/details.html"
    def get(self, request):
        return render(request, self.template)
################################# BLOG END ###################################


################################# SERVICES START ###################################

class ServicesView(View):
    template = "services/index.html"
    def get(self, request):
        return render(request, self.template)

################################# SERVICES END ###################################
