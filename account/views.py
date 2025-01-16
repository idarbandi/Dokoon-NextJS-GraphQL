import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST


def get_csrf(request):
    response = JsonResponse({'Info': "Successfully Set CSRF Cookie"})
    response['X-CSRFToken'] = get_token(request)
    return response


@require_POST
def Login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse(
            {"Info": "Username & Password Are Needed"}
        )
    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({
            "Info": "User Does Not Exist"
        }, status=400)
    login(request, user)
    return JsonResponse({
        "Info": "User Logged In Successfully"
    })
