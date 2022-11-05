from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'books'
    verbose_name = 'Книги'

    def ready(self):
        import books.signals
