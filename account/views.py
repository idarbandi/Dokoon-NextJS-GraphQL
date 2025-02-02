"""
********************************************************************************
 * 🌐 Dokoon-NextJS-GraphQL
 * 👤 Author: idarbandi
 * 📁 GitHub: https://github.com/idarbandi/Dokoon-NextJS-GraphQL
 * ✉️ Email: darbandidr99@gmail.com
 * 💼 LinkedIn: https://www.linkedin.com/in/amir-darbandi-72526b25b/
 *
 * This project was developed by idarbandi.
 * We hope you find it useful! Contributions and feedback are welcome.
 ********************************************************************************
"""

# این فایل ویوهای مربوط به برنامه حساب کاربری دکون رو تعریف می‌کنه

import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# تابعی برای گرفتن توکن CSRF و ارسالش به کلاینت
def dokoon_get_csrf_token(request):
    # توکن CSRF رو می‌گیریم
    token = get_token(request)
    print("CSRF Token sent to client:", token)  # نمایش توکن CSRF در لاگ سرور
    # توکن رو به صورت JSON می‌فرستیم
    return JsonResponse({'csrfToken': token})

# ویوی لاگین کاربر


@require_POST
def dokoon_login_view(request):
    # اطلاعات کاربر (نام کاربری و رمز عبور) رو از بدنه درخواست می‌گیریم
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    # چک می‌کنیم که نام کاربری و رمز عبور وارد شده باشن
    if username is None or password is None:
        return JsonResponse(
            {"پیام": "نام کاربری و رمز عبور الزامی هستند"},
            status=400
        )

    # احراز هویت کاربر
    user = authenticate(username=username, password=password)

    # اگه کاربر وجود نداشت یا اطلاعات نادرست بود
    if user is None:
        return JsonResponse({
            "پیام": "نام کاربری یا رمز عبور اشتباه است"
        }, status=400)

    # ورود کاربر به سیستم
    login(request, user)
    return JsonResponse({
        "پیام": "با موفقیت وارد شدید"
    })

# ویوی اطلاعات کاربر وارد شده


class dokoon_who_am_i_view(View):
    # متد GET برای دریافت اطلاعات کاربر
    def get(self, request):
        if request.user.is_authenticated:
            return JsonResponse({
                'username': request.user.username
            })
        else:
            return JsonResponse({
                'پیام': 'کاربری وارد نشده است'
            }, status=401)

# ویوی لاگ‌اوت کاربر


def dokoon_logout_view(request):
    # خروج کاربر از سیستم
    logout(request)
    return JsonResponse({'پیام': 'با موفقیت خارج شدید'})
