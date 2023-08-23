from django.contrib import admin

from .models import *


class BookShelfAdmin(admin.ModelAdmin):
    pass


admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Genres)
admin.site.register(Users)
admin.site.register(UserProperties)
admin.site.register(BookGenres)
admin.site.register(UserDictionary)
admin.site.register(Notes)
admin.site.register(Paragraphs)
admin.site.register(Tags)
admin.site.register(Styles)
admin.site.register(Countries)
admin.site.register(Languages)


