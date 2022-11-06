from django.db import models


class Reader(models.Model):
    name = models.TextField(verbose_name='Имя')
    email = models.TextField(verbose_name='Почта')
    rents = models.ManyToManyField('rents.Rent', blank=True, verbose_name='Аренды')
    fine = models.IntegerField(default=0, verbose_name='Штраф')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'