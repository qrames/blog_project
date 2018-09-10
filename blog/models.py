# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    short_descr = models.TextField()
    content = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    cover = models.ImageField(upload_to="article", height_field=None, width_field=None, max_length=100, null=True, blank=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    messages = models.TextField(max_length=20)
    date = models.DateTimeField(auto_now=True)

    article = models.ForeignKey('Article', on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ("-date",)

    def __unicode__(self):
        return '%s %s' % (self.full_name, self.date)

class Category(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)


    def __unicode__(self):
        return self.label

    def dislay(self):
        return self.label

    class Meta:
        verbose_name_plural = "Categories"
