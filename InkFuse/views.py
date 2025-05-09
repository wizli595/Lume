from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from inkwell.models import Article
from .utils import summarize_text, translate_text, generate_title_and_slug
from django.views.decorators.csrf import csrf_exempt
import json



@login_required
def summarize_article(request, slug):
   
    article = get_object_or_404(Article, slug=slug)
    summary = summarize_text(article.content)
    return JsonResponse({"summary": summary})

@login_required
def translate_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    lang = request.GET.get("lang", "French")
    translation = translate_text(article.content, lang)
    return JsonResponse({"translation": translation})

@login_required
def suggest_title_slug(request, slug):
    article = get_object_or_404(Article, slug=slug)
    title, slug = generate_title_and_slug(article.content)
    return JsonResponse({"title": title, "slug": slug})

@csrf_exempt
def suggest_title_slug_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            content = data.get("content", "")
            if not content:
                return JsonResponse({"error": "Missing content"}, status=400)
            title, slug = generate_title_and_slug(content)
            return JsonResponse({"title": title, "slug": slug})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)