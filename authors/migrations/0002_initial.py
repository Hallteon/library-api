# Generated by Django 4.1.3 on 2022-11-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_books',
            field=models.ManyToManyField(blank=True, null=True, to='books.book', verbose_name='Книги'),
        ),
    ]
