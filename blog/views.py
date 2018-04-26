from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def test(request):
	#return render(request, 'index.html', {'hello': 'Hello Blog...'})
	return render(request, 'blog/index.html')

def pagelist(request):
	articles = models.Article.objects.all()
	return render(request, 'blog/pagelist.html', {'articles': articles})

def article_page(request, article_id):
	article = models.Article.objects.get(pk = article_id)
	return render(request, 'blog/article_page.html', {'article': article})
