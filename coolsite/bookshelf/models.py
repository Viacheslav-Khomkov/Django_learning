from django.db import models


class Styles(models.Model):  # классы для CSS
    name = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)  # Название класса для оформления


class Paragraphs(models.Model):  # Абзацы книг
    line = models.IntegerField()  # номер абзаца в книге
    book_id = models.IntegerField()  # Ссылка на книгу
    tag_id = models.IntegerField()  # Ссылка на тэг HTML
    chapter_id = models.IntegerField()  # индекс главы (для отображения по главам)
    text = models.TextField(blank=True)  # Текст абзаца

class Notes(models.Model):
    par_id = models.IntegerField()  # абзаца в книге
    book_id = models.IntegerField()  # Ссылка на книгу
    text = models.TextField(blank=True)  # Текст абзаца


class UserDictionary(models.Model):
    user_id = models.IntegerField()  # Ссылка на пользователя
    book_id = models.IntegerField()  # Ссылка на книгу - если не задана - настройка общая
    source = models.CharField(max_length=255)
    translate = models.CharField(max_length=255)


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class UserProperties(models.Model):  # Настройки внешнего вида страницы для каждого пользователя и каждой книги
    user_id = models.IntegerField()  # Ссылка на пользователя
    style_id = models.IntegerField()  # Ссылка на основной стиль пользователя
    book_id = models.IntegerField(blank=True)  # Ссылка на книгу - если не задана - настройка общая


class Books(models.Model):
    author_id = models.IntegerField()
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateField()
    isbn = models.CharField(max_length=20)
    lang_id = models.IntegerField()


class Authors(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    country_id = models.IntegerField()
    lang_id = models.IntegerField()


class Countries(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)
    lang_id = models.IntegerField()


class Languages(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=10)



