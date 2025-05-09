from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'created_at', 'is_deleted')
    list_filter = ('created_at', 'is_deleted')
    search_fields = ('content', 'author__username', 'article__title')
