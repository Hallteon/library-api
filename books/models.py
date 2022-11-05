from django.db import models


class Book(models.Model):
    name = models.TextField(verbose_name='Имя')
    max_period = models.IntegerField(verbose_name='Максимальный период аренды')
    cover = models.TextField(verbose_name='Обложка')
    book_author = models.ForeignKey('authors.Author', related_name='book', on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.book_author.author_books.add()

        super(Book, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'