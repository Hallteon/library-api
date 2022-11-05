# Generated by Django 4.1.3 on 2022-11-05 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('max_period', models.IntegerField(verbose_name='Максимальный период аренды')),
                ('cover', models.TextField(verbose_name='Обложка')),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
