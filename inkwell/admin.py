from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'deleted_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'deleted_at')
    prepopulated_fields = {'slug': ('title',)}
