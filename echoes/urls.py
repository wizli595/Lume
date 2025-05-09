from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:article_id>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/like/<int:comment_id>/', views.CommentLikeToggleView.as_view(), name='comment_like_toggle'),
    path('comment/delete/<int:comment_id>/', views.CommentSoftDeleteView.as_view(), name='comment_soft_delete'),
]
