from django.shortcuts import render

from CPDM.accounts.models import Profile


def get_profile():                  # check if profile is logged in
    return Profile.objects.first()


def index(request):
    profile = get_profile()

    if profile is None:
        return render(request, 'web/home-no-profile.html')

    return render(request, 'web/home-with-profile.html')
