import graphene
from graphene_django import DjangoObjectType

from .models import DokoonProduct as product


class ProductType(DjangoObjectType):
    class Meta:
        model = product
        fields = ('id', 'title', 'description', 'regular_price', 'slug')


class Query(graphene.ObjectType):
    main_index = graphene.List(ProductType)

    def resolve_main_index(root, info):
        return product.objects.all()


schema = graphene.Schema(query=Query)
