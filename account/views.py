"""********************************************************************************
 * Dokoon Project
 * Author: Idarbandi
 * GitHub: https://github.com/idarbandi/Dokoon-NextDRF
 * Email: darbandidr99@gmail.com
 *
 * This project was developed by Idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 *********************************************************************************

"""

# این فایل نما‌های مربوط به برنامه account را تعریف می‌کند.
# (This file defines the views for the account application.)

import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# تابعی برای دریافت توکن CSRF و تنظیم کوکی آن
# (Function to get CSRF token and set its cookie)
def get_csrf(request):
    response = JsonResponse(
        {'اطلاعات': "کوکی CSRF با موفقیت تنظیم شد"})  # Info in Farsi
    response['X-CSRFToken'] = get_token(request)
    return response


# نما (view) برای ورود به سیستم
# (View for login)
@require_POST
def Login_view(request):
    # دریافت اطلاعات ورود از بدنه درخواست (request body)
    # (Get login information from request body)
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    # بررسی صحت اطلاعات ورود
    # (Validate login information)
    if username is None or password is None:
        return JsonResponse(
            {"اطلاعات": "نام کاربری و رمز عبور الزامی هستند"}  # Info in Farsi
        )
    user = authenticate(username=username, password=password)

    # کاربر یافت نشد
    # (User not found)
    if user is None:
        return JsonResponse({
            "اطلاعات": "کاربر وجود ندارد"
        }, status=400)

    # ورود کاربر به سیستم
    # (Login user)
    login(request, user)
    return JsonResponse({
        "اطلاعات": "کاربر با موفقیت وارد سیستم شد"
    })


# نمای who_am_i برای بازیابی اطلاعات کاربر لاگین‌شده
# (who_am_i view to retrieve logged-in user information)
class who_am_i_view(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    # متد get برای بازیابی اطلاعات کاربر
    # (get method to retrieve user information)
    @staticmethod
    def get(request, format=None):
        return JsonResponse({
            'username': request.user.username
        })


def Logout_view(request):
    logout(request)
    return JsonResponse({'detail': 'Successfully logged out'})
