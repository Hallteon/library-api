# Generated by Django 4.1.3 on 2022-11-05 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_alter_author_author_books'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='authors.author', verbose_name='Автор'),
        ),
    ]
