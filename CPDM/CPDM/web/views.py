from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def index(request):
    user = request.user
    pk = user.pk

    context = {
        'pk': pk,
        'profile': user,
    }

    if user.is_anonymous:
        return render(request, 'web/home-no-profile.html')

    return render(request, 'web/home-with-profile.html', context)


def about(request):
    return render(request, 'web/about.html')
