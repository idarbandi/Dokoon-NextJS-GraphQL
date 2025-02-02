"""
********************************************************************************
🌐 Dokoon Project
👤 Author: idarbandi
📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
✉️ Email: darbandidr99@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/

This project was developed by idarbandi.
We hope you find it useful! Contributions and feedback are welcome.
********************************************************************************
"""

import graphene
import graphql_jwt
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


# تعریف نوع کاربر دکون برای GraphQL
class DokoonUserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", 'username', "email")

# تعریف کوئری‌های دکون


class DokoonQuery(graphene.ObjectType):
    user_details = graphene.Field(DokoonUserType)

    def resolve_user_details(self, info, **kwargs):
        # این متد جزئیات کاربر احراز هویت شده را بازمی‌گرداند
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("اعتبارسنجی انجام نشده است")
        return User.objects.get(username=user)

# تعریف Mutation برای خروج کاربر


class DokoonLogoutMutation(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    @login_required
    def mutate(self, info):
        # این متد کاربر را از سیستم خارج می‌کند
        info.context.session.flush()
        return DokoonLogoutMutation(success=True)

# تعریف Mutation‌های دکون


class DokoonMutation(graphene.ObjectType):
    logout = DokoonLogoutMutation.Field()
    # Mutation‌های مربوط به احراز هویت JWT
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
