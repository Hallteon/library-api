import graphene
from graphene import ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType

from readers.models import Reader
from readers.serializers import ReaderSerializer


class ReaderType(DjangoObjectType):
    class Meta:
        model = Reader


class ReaderInput(graphene.InputObjectType):
    id = graphene.ID()


class Query(ObjectType):
    reader = graphene.Field(ReaderType, id=graphene.Int())
    readers = graphene.List(ReaderType)

    def resolve_reader(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Reader.objects.get(pk=id)

        return None

    def resolve_readers(self, info, **kwargs):
        return Reader.objects.all()


class ReaderSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = ReaderSerializer
        model_operations = ['create', 'update', 'delete']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    edit_readers = ReaderSerializerMutation.Field()
