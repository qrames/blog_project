# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
# from django.views.generic.list import ListView
from django.urls import reverse
from django.utils import timezone
from .models import Article, Category, Comment
from .form import CommentForm
from datetime import datetime
# Create your views here.
class IndexView(ListView):
    model = Article
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = ListView.get_context_data(self, *args, **kwargs)
        context['categories'] = Category.objects.all()

        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        query_date = self.request.GET.get('search_date_from', None)
        # print "QUERY=", query
        if query != None:
            return Article.objects.filter(title__contains=query)

        elif query_date != None:
            date = datetime.strptime(query_date, '%d/%m/%Y')
            return Article.objects.filter(published_at__date=date.date())

        else:
            return Article.objects.all()

# Create your views here.

class ArticleDetailView(DetailView):

    model = Article

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)

        comment_form_initial = {
            'article': self.get_object()
        }

        context['comment_form'] = CommentForm(initial=comment_form_initial)

        return context

class CategoryView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = DetailView.get_context_data(self, *args, **kwargs)
        context['categories'] = Category.objects.all()

        # context['article'] = Article.objects.filter(category = self.get_object())

        return context

class CommentCreateView(CreateView):
    model = Comment
    fields = "__all__"
    # success_url = "/"
    def get_success_url(self):
        return reverse("article-detail", args=[self.object.article.slug])
