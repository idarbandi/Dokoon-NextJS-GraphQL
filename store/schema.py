import graphene
from graphene_django import DjangoObjectType

from .models import DokoonCategory as Category
from .models import DokoonProduct as Product
from .models import DokoonProductImage as ProductImage


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'alt_text')

    def resolve_image(self, info):
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'regular_price',
                  'slug', 'product_image', 'product_category')


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'product_category')


class Query(graphene.ObjectType):
    main_index = graphene.List(ProductType)
    category_index = graphene.Field(
        CategoryType, name=graphene.String(required=True))
    main_index_by_name = graphene.Field(
        ProductType, slug=graphene.String(required=True))
    all_slugs = graphene.List(graphene.String)

    def resolve_main_index_by_name(root, info, slug):
        try:
            return Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            return None

    def resolve_category_index(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def resolve_main_index(root, info):
        return Product.objects.all()

    def resolve_all_slugs(root, info):
        return Product.objects.values_list('slug', flat=True)


schema = graphene.Schema(query=Query)
