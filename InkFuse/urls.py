from django.urls import path
from . import views

urlpatterns = [
    path("suggest/", views.suggest_title_slug_api, name="suggest_title_slug_api"),
    path('<slug:slug>/summarize/', views.summarize_article, name='summarize_article'),
    path('<slug:slug>/translate/', views.translate_article, name='translate_article'),
    path('<slug:slug>/suggest/', views.suggest_title_slug, name='suggest_title_slug'),
]
