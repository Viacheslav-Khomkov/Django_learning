from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, "women/index.html", context=context)


def about(request):
    return render(request, "women/about.html",
                  {'menu': menu, 'title': 'About'})


def categories(request, cat_id):
    if request.GET:
        for par in request.GET:
            print(par, request.GET[par])
    return HttpResponse(f"<h1>Статьи по категориям women</h1><p>{cat_id}</p>")


def add_page(request):
    return HttpResponse(f"<h1>Добавление статьи</h1>")


def contact(request):
    return HttpResponse(f"<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse(f"<h1>Авторизация</h1>")



def show_post(request, post_id):
    return HttpResponse(f"<h1>Статья с id = {post_id}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
