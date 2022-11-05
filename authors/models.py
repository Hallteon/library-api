from django.db import models


class Author(models.Model):
    name = models.TextField(verbose_name='Название')
    link = models.TextField(verbose_name='Ссылка')
    birth_day = models.TextField(verbose_name='Дата рождения')
    death_day = models.TextField(blank=True, verbose_name='Дата смерти')
    author_books = models.ManyToManyField('books.Book', blank=True, verbose_name='Книги')
    available_books = models.IntegerField(verbose_name='Количество доступных для аренды книг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
