from django.db import models


class Rent(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, verbose_name='Книга')
    book_reader = models.ForeignKey('readers.Reader', on_delete=models.CASCADE, verbose_name='Читатель')
    rent_time = models.DateTimeField(auto_now_add=True, verbose_name='Время аренды')
    period = models.IntegerField(default=0, verbose_name='Период аренды')
    fine_size = models.IntegerField(verbose_name='Размер штрафа за день просрочки')

    def __str__(self):
        return self.book.name

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'