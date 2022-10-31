from django.db import models


class Author(models.Model):
    name = models.TextField(verbose_name='Имя')
    link = models.TextField(verbose_name='Ссылка')
    birth_day = models.TextField(verbose_name='Дата рождения')
    death_day = models.TextField(verbose_name='Дата смерти')
    books = models.ManyToManyField('books.Book', verbose_name='Книги')
    available_books = models.IntegerField(verbose_name='Количество доступных для аренды книг')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
