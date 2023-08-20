from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Главная страница приложения Women")


def categories(request, catid):
    if request.GET:
        for par in request.GET:
            print(par, request.GET[par])
    return HttpResponse(f"<h1>Статьи по категориям women</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по году {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

