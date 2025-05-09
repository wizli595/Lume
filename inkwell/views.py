from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm
from django.db.models import Q
from echoes.forms import CommentForm

class ArticleListView(ListView):
    model = Article
    template_name = "inkwell/article_list.html"
    context_object_name = "articles"




    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.active()

        # If user is authenticated, show their own hidden articles too
        if user.is_authenticated:
            queryset = queryset.filter(
                Q(hidden=False) | Q(author=user)
            )
        else:
            queryset = queryset.filter(hidden=False)

        return queryset

class MyArticlesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "inkwell/my_articles.html"
    context_object_name = "articles"

    def get_queryset(self):
        return self.request.user.articles.active()


class ArticleDetailView(DetailView):
    model = Article
    template_name = "inkwell/article_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "inkwell/article_form.html"
    success_url = reverse_lazy("article_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Article created successfully!")
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "inkwell/article_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"slug": self.object.slug})


@login_required
def article_soft_delete(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.soft_delete()
    messages.warning(request, "🗑️ Article moved to trash.")
    return redirect("my_articles")


class DeletedArticlesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "inkwell/article_trash.html"
    context_object_name = "articles"

    def get_queryset(self):
        return self.request.user.articles.deleted()


@login_required
def article_restore(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.restore()
    messages.success(request, "♻️ Article restored successfully.")

    return redirect("article_trash")

@login_required
def unlock_article(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.hidden = False
    article.save()
    messages.success(request, "🔓 Article unlocked successfully.")
    return redirect("article_detail", slug=slug)
