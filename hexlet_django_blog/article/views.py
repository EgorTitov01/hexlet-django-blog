from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.shortcuts import render
from django.views import View
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

MESSAGE_TAGS = {
    messages.SUCCESS: "alert alert-success",
}

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        storage = messages.get_messages(request)
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
                'messages': storage
            },
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = get_object_or_404(Article, id=article_id)
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )

class ArticleCreateView(View):

    template = 'articles/create.html'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request, self.template,
            context = {'form': form}
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Статья успешно создана')
            return redirect('articles_index')

        return render(
            request, self.template,
            context = {'form': form}
        )

class ArticleEditView(View):
    template = 'articles/update.html'

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, self.template,
            context = {'form': form, 'article_id': article_id,}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Статья успешно отредактирована')
            return redirect('articles_index')

        return render(
            request, "articles/update.html",
            {"form": form, "article_id": article_id}
        )

class ArticleDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        messages.success(request, 'Статья успешно удалена')
        return redirect('articles_index')
