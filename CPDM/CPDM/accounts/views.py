from django.contrib.auth import views as auth_views, authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from CPDM.accounts.forms import AccountUserCreationForm, AccountLoginForm


class LoginUserView(views.View):
    form_class = AccountLoginForm   # use django auth form

    # overwrite get() method and set the form in the context
    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class(),          # take form_class
        }
        return render(request, 'accounts/login.html', context)

    # overwrite post() method and set the username and password in the request and authenticate()
    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST or None)
        # if form.is_valid():
        email, password = request.POST['username'], request.POST['password']

        user = authenticate(username=email, password=password)
        # print(user)

        if user is not None:
            # add user to session
            login(request, user)

        return redirect('index')


class RegisterUserView(views.CreateView):
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'       # choose template
    success_url = reverse_lazy('index')


# superuser:    Danioo
# Password:     DanDan123

# email:    dan@dan.com
# Password: 123


def logout_view(request):
    logout(request)
    # Redirect to a page after logout (optional)
    return redirect('index')


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
