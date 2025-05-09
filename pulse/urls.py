from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeFeedView.as_view(), name='home_feed'),
    path('trending/', views.TrendingFeedView.as_view(), name='trending_feed'),
    path('following/', views.FollowingFeedView.as_view(), name='following_feed'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]
