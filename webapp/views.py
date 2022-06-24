from django.shortcuts import render

from webapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)
    return render(request, 'index.html', context)


def create_article(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        description = request.POST.get("title")
        status = request.POST.get("author")
        date = request.POST.get("content")
        new_article = Article.objects.create(description=description, status=status, date=date)
        context = {"article": new_article}
        return render(request, "article_view.html", context)
