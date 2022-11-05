import graphene
from graphene import ObjectType, Argument
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType
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


class BookInput(graphene.InputObjectType):
    id = graphene.ID()


class ReturnBook(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        book_id = graphene.Int(BookInput)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Rent.objects.get(book=kwargs.get('book_id'))
        obj.delete()

        return cls(ok=True)


class RentSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = RentSerializer
        model_operations = ['create']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    rent_book = RentSerializerMutation.Field()
    return_book = ReturnBook.Field()
