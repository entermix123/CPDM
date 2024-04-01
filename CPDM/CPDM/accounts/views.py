from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from CPDM.accounts.forms import AccountUserCreationForm, AccountLoginForm
from CPDM.accounts.models import Profile


UserModel = get_user_model()


class LoginUserView(LoginView):
    form_class = AccountLoginForm   # use django auth form
    template_name = 'accounts/login.html'

    # overwrite get() method and set the form in the context
    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class(),          # take form_class
        }
        return render(request, 'accounts/login.html', context)

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            login(self.request, user)
            return redirect('index')
        else:
            messages.error(self.request, 'Invalid email or password.')
            return self.form_invalid(form)


class RegisterUserView(views.CreateView):
    form_class = AccountUserCreationForm
    template_name = 'accounts/register.html'       # choose template
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        super(RegisterUserView, self).form_valid(form)
        username = form.cleaned_data['email']
        raw_password = form.cleaned_data['password1']
        user = authenticate(email=username, password=raw_password)
        login(self.request, user)

        return redirect('index')


# dan@dan.com
# 123


class UpdateProfileView(LoginRequiredMixin, views.UpdateView):
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('index')
    template_name = 'accounts/profile_update.html'

    def get_queryset(self):
        user_pk = self.request.user.pk
        queryset = Profile.objects.filter(pk=user_pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.request.user.pk})


@login_required
def logout_view(request, pk):
    logout(request)
    # Redirect to a page after logout (optional)
    return redirect('index')


class ProfileDetailView(LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['companies_owned'] = user.companies.all()
        context['activities_owned'] = user.activities.all()

        return context

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.request.user.pk})


class DeleteUserView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['profile'] = user

        return context
