# accounts/views.py
import json

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.test import Client, TestCase
from django.urls import path, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import views


def get_csrf(request):
    response = JsonResponse({'اطلاعات': "کوکی CSRF با موفقیت تنظیم شد"})
    response['X-CSRFToken'] = get_token(request)
    return response


@csrf_exempt
@require_POST  # Keep require_POST for this view
def Login_view(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            # Correct status code
            return JsonResponse({'اطلاعات': "نام کاربری و رمز عبور الزامی هستند"}, status=200)

        user = authenticate(request, username=username, password=password)

        if user is None:
            return JsonResponse({'اطلاعات': "کاربر وجود ندارد"}, status=400)

        login(request, user)
        return JsonResponse({'اطلاعات': "کاربر با موفقیت وارد سیستم شد"})

    except json.JSONDecodeError:
        return JsonResponse({'detail': "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({'detail': f"An error occurred: {str(e)}"}, status=500)


@csrf_exempt
def Logout_view(request):
    logout(request)
    return JsonResponse({'detail': 'Successfully logged out'})


class who_am_i_view(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return JsonResponse({'username': request.user.username})


# accounts/urls.py

app_name = 'account'

urlpatterns = [
    path('csrf/', views.get_csrf, name='api_csrf'),
    path('login/', views.Login_view, name='api_login'),
    path('logout/', views.Logout_view, name='api_logout'),
    path('whoami/', views.who_am_i_view.as_view(), name='whoami'),
]

# accounts/tests.py

User = get_user_model()


class AccountsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_get_csrf(self):
        url = reverse('account:api_csrf')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('X-CSRFToken', response)
        self.assertJSONEqual(response.content, {
                             'اطلاعات': "کوکی CSRF با موفقیت تنظیم شد"})

    def test_login_view_valid(self):
        url = reverse('account:api_login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
                             'اطلاعات': "کاربر با موفقیت وارد سیستم شد"})
        self.assertTrue(self.client.login(
            username='testuser', password='testpassword'))

    def test_login_view_invalid_credentials(self):
        url = reverse('account:api_login')
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(url, json.dumps(
            data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'اطلاعات': "کاربر وجود ندارد"})
        self.assertFalse(self.client.login(
            username='testuser', password='wrong'))
