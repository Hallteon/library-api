import graphene
from graphene import ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType
from books.models import Book
from books.serializers import BookSerializer
from rents.models import Rent
from rents.serializers import RentSerializer


class RentType(DjangoObjectType):
    class Meta:
        model = Rent


class Query(ObjectType):
    rent = graphene.Field(RentType, id=graphene.Int())
    rents = graphene.List(RentType)

    def resolve_rent(self, info, **kwargs):
        id = kwargs.get('id')

        if id:
            return Rent.objects.get(pk=id)

        return None

    def resolve_rents(self, info, **kwargs):
        return Rent.objects.all()


class RentSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = RentSerializer
        model_operations = ['create', 'update', 'delete']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    edit_rents = RentSerializerMutation.Field()