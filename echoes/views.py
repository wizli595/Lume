from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Comment
from inkwell.models import Article
from django.shortcuts import render

class CommentListView(ListView):
    model = Comment
    template_name = 'echoes/comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        article = get_object_or_404(Article, slug=self.kwargs['slug'], deleted_at__isnull=True)
        return Comment.objects.filter(article=article, parent__isnull=True, is_deleted=False).select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, slug=self.kwargs['slug'])
        return context


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id, deleted_at__isnull=True)
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        parent = Comment.objects.filter(id=parent_id).first() if parent_id else None

        if content:
            Comment.objects.create(
                article=article,
                author=request.user,
                content=content,
                parent=parent
            )
            messages.success(request, "💬 Comment posted.")
        else:
            messages.error(request, "❌ Comment cannot be empty.")

        return redirect('article_detail', slug=article.slug)



class CommentLikeToggleView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        return render(request, "echoes/partials/comment_like_button.html", {
            "comment": comment,
            "user": request.user,
        })



class CommentSoftDeleteView(LoginRequiredMixin, View):
    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, author=request.user)
        comment.is_deleted = True
        comment.save()
        messages.warning(request, "🗑️ Comment deleted.")
        return redirect('article_detail', slug=comment.article.slug)
