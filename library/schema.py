import graphene

import authors.schema
import books.schema
import readers.schema
import rents.schema


class Query(books.schema.Query, authors.schema.Query, rents.schema.Query, readers.schema.Query, graphene.ObjectType):
    pass


class Mutation(books.schema.Mutation, authors.schema.Mutation, rents.schema.Mutation, readers.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)