from django.db import models


class Rent(models.Model):
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, verbose_name='Книга')
    book_reader = models.ForeignKey('readers.Reader', on_delete=models.CASCADE, verbose_name='Читатель')
    rent_time = models.TextField(verbose_name='Время аренды')
    period = models.TextField(verbose_name='Период аренды')
    fine_size = models.IntegerField(verbose_name='Размер штрафа за день просрочки')

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'