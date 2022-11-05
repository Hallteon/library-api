from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Book


@receiver(post_save, sender=Book)
def add_book(sender, instance, created, **kwargs):
    if created:
        instance.book_author.author_books.add(instance)