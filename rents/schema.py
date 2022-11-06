from datetime import datetime

import graphene
from django.db.models import F
from graphene import ObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django.types import DjangoObjectType

from books.schema import BookInput
from readers.models import Reader
from readers.schema import ReaderInput
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


class ReturnBook(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        book_id = graphene.Int(BookInput)
        reader_id = graphene.Int(ReaderInput)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        objs = Rent.objects.filter(book_id=kwargs.get('book_id'), book_reader_id=kwargs.get('reader_id'))

        for obj in objs:
            time_rent = datetime.now() - obj.rent_time.replace(tzinfo=None)
            days = time_rent.days

            if days > obj.period:
                fine_days = days - obj.period
                reader_obj = Reader.objects.get(id=kwargs.get('reader_id'))
                reader_obj.fine = reader_obj.fine + (fine_days * obj.fine_size)

                reader_obj.save()

        if list(objs):
            objs.delete()

            return cls(ok=True)


class RentSerializerMutation(SerializerMutation):
    class Meta:
        serializer_class = RentSerializer
        model_operations = ['create']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    rent_book = RentSerializerMutation.Field()
    return_book = ReturnBook.Field()
