# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from  .models import Article, Comment, Category
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'published_at')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ("Général", {
            'fields':   (('title', 'slug', 'cover'),
                        ('category', 'published_at'),
                    ),
            }),
        ("Contenu", {
            'fields': ('short_descr', 'content')
        }),
    )
    search_fields = ('title', 'content', 'short_descr')


class CommentAdmin(admin.ModelAdmin):

    fieldsets = (
        ("YOUR CONTACT :", {
            'fields':   (('full_name', 'email'),),
            }),
        ("Article sible :", {
            'fields':   (('article', 'parent'),),
            }),
        ("YOUR COMMENT :", {
            'fields':   (('messages', ),),
            }),
    )
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('label',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
