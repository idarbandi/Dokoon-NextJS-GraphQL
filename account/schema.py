import graphene
import graphql_jwt
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", 'username', "email")


class Query(graphene.ObjectType):
    user_details = graphene.Field(UserType)

    def resolve_user_details(root, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication Credentials Were Not Provided")
        return User.objects.get(username=user)


class LogoutMutation(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    @login_required
    def mutate(self, info):
        info.context.session.flush()
        return LogoutMutation(success=True)


class Mutation(graphene.ObjectType):
    logout = LogoutMutation.Field()
    # Include other mutations like token authentication if using JWT
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
