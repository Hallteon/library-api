import graphene
from graphene import ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    authors = graphene.List(AuthorType)

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Author.objects.get(pk=id)

        return None

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()


class AuthorSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = AuthorSerializer
        model_operations = ['create', 'update', 'delete']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    edit_authors = AuthorSerializerMutation.Field()