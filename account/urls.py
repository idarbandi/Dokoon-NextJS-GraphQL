from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path("csrf/", views.get_csrf, name="api_csrf"),
    path("login/", views.Login_view, name="api_login"),
    # path("whoami/", views.whoAmIview, name="whoami")
]
