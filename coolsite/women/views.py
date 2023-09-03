from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

#
# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'},
#         ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        # 'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
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
    post = get_object_or_404(Women, pk=post_id)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,

    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        # 'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, "women/index.html", context=context)
    # return HttpResponse(f"<h1>Категория с id = {cat_id}</h1>")



def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
