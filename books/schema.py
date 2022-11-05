import graphene
from graphene import ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType
from books.models import Book
from books.serializers import BookSerializer


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(ObjectType):
    book = graphene.Field(BookType, id=graphene.Int())
    books = graphene.List(BookType)

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Book.objects.get(pk=id)

        return None

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()


class BookSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = BookSerializer
        model_operations = ['create', 'update', 'delete']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    edit_books = BookSerializerMutation.Field()