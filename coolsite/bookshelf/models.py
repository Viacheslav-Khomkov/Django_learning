from django.db import models


class Styles(models.Model):  # классы для CSS
    name = models.CharField(max_length=100, db_index=True)
    class_name = models.CharField(max_length=100)  # Название класса для оформления

    def __str__(self):
        return f'{self.name}'


class Tags(models.Model):  # классы для CSS
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return f'{self.name}'


class Paragraphs(models.Model):  # Абзацы книг
    book = models.ForeignKey('Books', on_delete=models.PROTECT)
    tag = models.ForeignKey('Tags', on_delete=models.PROTECT, null=True)  # Ссылка на тэг HTML
    text = models.TextField(blank=True)  # Текст абзаца


class Notes(models.Model):
    par_id = models.ForeignKey('Paragraphs', on_delete=models.PROTECT)  # абзаца в книге
    book = models.ForeignKey('Books', on_delete=models.PROTECT)
    text = models.TextField(blank=True)  # Текст абзаца


class UserDictionary(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT)  # Ссылка на пользователя
    book = models.ForeignKey('Books', on_delete=models.PROTECT)
    original = models.CharField(max_length=255)
    translate = models.CharField(max_length=255)


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    lang = models.ForeignKey('Languages', on_delete=models.PROTECT, null=True)  # Язык пользователя

    def __str__(self):
        return f'{self.name}'


class UserProperties(models.Model):  # Настройки внешнего вида страницы для каждого пользователя и каждой книги
    user = models.ForeignKey('Users', on_delete=models.PROTECT)  # Ссылка на пользователя
    style = models.ForeignKey('Styles', on_delete=models.PROTECT)  # Ссылка на основной стиль пользователя
    book = models.ForeignKey('Books', on_delete=models.PROTECT, null=True)
    lang = models.ForeignKey('Languages', on_delete=models.PROTECT, null=True)  # Язык пользователя


class Genres(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return f'{self.name}'


class BookGenres(models.Model):
    book = models.ForeignKey('Books', on_delete=models.PROTECT)
    genre = models.ForeignKey('Genres', on_delete=models.PROTECT)

class Books(models.Model):
    author = models.ForeignKey('Authors', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date = models.DateField()
    isbn = models.CharField(max_length=20)
    lang = models.ForeignKey('Languages', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'


class Authors(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True)
    time_update = models.DateTimeField(auto_now=True)
    country = models.ForeignKey('Countries', on_delete=models.PROTECT, null=True)
    lang = models.ForeignKey('Languages', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.name}'

class Countries(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    short_name = models.CharField(max_length=10)
    lang = models.ForeignKey('Languages', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.name}'


class Languages(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} ({self.short_name})'




