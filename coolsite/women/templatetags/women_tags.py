from django import template
from women.models import *

register = template.Library()

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]

@register.simple_tag(name='cats')
def get_categories(_filter=None):
    if not _filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=_filter)

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('women/main_menu.html')
def show_main_menu():
    return {"menu": menu}

