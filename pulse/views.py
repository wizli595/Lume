from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from django.db.models import Count
from inkwell.models import Article
from .models import Follow
from persona.models import CustomUser

class HomeFeedView(LoginRequiredMixin, ListView):
    template_name = 'pulse/home_feed.html'
    context_object_name = 'articles'

    def get_queryset(self):
        following_users = self.request.user.following_set.values_list('following_id', flat=True)
        return Article.objects.filter(author__id__in=following_users, deleted_at__isnull=True).filter(Q(hidden=False) | Q(author=self.request.user)).order_by('-created_at')


class TrendingFeedView(ListView):
    template_name = 'pulse/trending_feed.html'
    context_object_name = 'articles'

    def get_queryset(self):
        recent_time = timezone.now() - timedelta(days=3)

        return (
            Article.objects
            .filter(created_at__gte=recent_time, deleted_at__isnull=True, hidden=False)
            .annotate(comment_count=Count('comments', filter=Q(comments__is_deleted=False)))
            .filter(comment_count__gt=2)
            .order_by('-comment_count', '-created_at')
        )

class FollowingFeedView(LoginRequiredMixin, ListView):
    template_name = 'pulse/following_feed.html'
    context_object_name = 'articles'

    def get_queryset(self):
        following_users = self.request.user.following_set.values_list('following_id', flat=True)
        return Article.objects.filter(author__in=following_users, deleted_at__isnull=True).filter(Q(hidden=True) | Q(author=self.request.user))


@login_required
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    if target_user != request.user:
        Follow.objects.get_or_create(follower=request.user, following=target_user)
        messages.success(request, f"✅ You are now following {target_user.username}.")
    return redirect('profile', username=target_user.username)


@login_required
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    Follow.objects.filter(follower=request.user, following=target_user).delete()
    messages.warning(request, f"🚫 You have unfollowed {target_user.username}.")
    return redirect('profile', username=target_user.username)
