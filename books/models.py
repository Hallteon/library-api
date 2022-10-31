from django.db import models


class Book(models.Model):
    name = models.TextField(verbose_name='Имя')
    max_period = models.TextField(verbose_name='Максимальный период аренды')
    cover = models.TextField(verbose_name='Обложка')
    book_author = models.ForeignKey('books.Book', on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'