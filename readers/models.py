from django.db import models


class Reader(models.Model):
    name = models.TextField(verbose_name='Имя')
    email = models.TextField(verbose_name='Почта')
    rents = models.ManyToManyField('rents.Rent', verbose_name='Аренды')
    fine = models.IntegerField(verbose_name='Штраф')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'