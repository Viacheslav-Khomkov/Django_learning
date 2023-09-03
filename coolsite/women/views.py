from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
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
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, "women/index.html", context=context)


def about(request):
    return render(request, "women/about.html",
                  {'title': 'About', })


# def categories(request, cat_id):
#     if request.GET:
#         for par in request.GET:
#             print(par, request.GET[par])
#     return HttpResponse(f"<h1>Статьи по категориям women</h1><p>{cat_id}</p>")


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()

    return render(request, 'women/addpage.html',
                  {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse(f"<h1>Обратная связь</h1>")


def login(request):
    return HttpResponse(f"<h1>Авторизация</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
        'cat_slug_selected': post.cat.slug,

    }
    return render(request, 'women/post.html', context=context)


# def show_category(request, cat_id):
def show_category(request, cat_slug):

    cat = Category.objects.get(slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat.pk)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug,
    }
    return render(request, "women/index.html", context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")
