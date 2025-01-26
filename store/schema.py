import graphene
from graphene_django import DjangoObjectType

from .models import DokoonProduct as product
from .models import DokoonProductImage as ProductImage


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        field = ('id', 'image', 'alt_text')

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


class ProductType(DjangoObjectType):
    class Meta:
        model = product
        fields = ('id', 'title', 'description',
                  'regular_price', 'slug', 'product_image')


class Query(graphene.ObjectType):
    main_index = graphene.List(ProductType)

    def resolve_main_index(root, info):
        return product.objects.all()


schema = graphene.Schema(query=Query)
