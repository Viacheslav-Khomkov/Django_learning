from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Women.objects.all()
    return render(request,"women/index.html",
                  {'posts': posts, 'menu': menu, 'title': 'Women'})


def about(request):
    return render(request,"women/about.html",
    {'menu': menu, 'title': 'About'})


def categories(request, cat_id):
    if request.GET:
        for par in request.GET:
            print(par, request.GET[par])
    return HttpResponse(f"<h1>Статьи по категориям women</h1><p>{cat_id}</p>")


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по году {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

