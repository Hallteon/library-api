# Generated by Django 4.1.3 on 2022-11-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('authors', '0003_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_books',
            field=models.ManyToManyField(blank=True, to='books.book', verbose_name='Книги'),
        ),
    ]