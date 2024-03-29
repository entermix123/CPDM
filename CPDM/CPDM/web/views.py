from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def get_profile():                  # check if profile is logged in
    return UserModel.objects.first()


def index(request):
    user = request.user

    if user.is_anonymous:
        return render(request, 'web/home-no-profile.html')

    return render(request, 'web/home-with-profile.html')


def about(request):
    return render(request, 'web/about.html')
