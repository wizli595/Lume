from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('new/', views.ArticleCreateView.as_view(), name='article_create'),
    path('my/', views.MyArticlesView.as_view(), name='my_articles'),
    path('trash/', views.DeletedArticlesView.as_view(), name='article_trash'),
    path('trash/<slug:slug>/restore/', views.article_restore, name='article_restore'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<slug:slug>/delete/', views.article_soft_delete, name='article_delete'),
     path('articles/<slug:slug>/unlock/', views.unlock_article, name='unlock_article'),
]
