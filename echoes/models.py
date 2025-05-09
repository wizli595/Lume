from django.db import models
from django.conf import settings
from django.utils import timezone
from inkwell.models import Article

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    # Likes
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_echoes", blank=True)

    # Optional for replies (threaded comments)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    # Soft delete
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} on {self.article.title[:20]}"

    def like_count(self):
        return self.likes.count()

    def is_reply(self):
        return self.parent is not None

    def is_visible(self):
        return not self.is_deleted

