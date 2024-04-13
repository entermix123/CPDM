from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from rest_framework import generics, permissions
from rest_framework.authtoken import views as token_views

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from CPDM.accounts.forms import AccountUserCreationForm, AccountLoginForm
from CPDM.accounts.models import Profile
from CPDM.accounts.serielizers import UserRegisterSerializer, ProfileSerializer, UserSerializer, \
    ProfileUpdateSerializer, UserDeleteSerializer

UserModel = get_user_model()


class LoginUserView(LoginView):
    form_class = AccountLoginForm  # use django auth form
    template_name = 'accounts/login.html'

    # overwrite get() method and set the form in the context
    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class(),  # take form_class
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
    template_name = 'accounts/register.html'  # choose template
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
        context['profile'] = Profile.objects.get(pk=self.request.user.pk)

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
        user = (UserModel.objects
                .prefetch_related('companies', 'activities')
                .get(pk=self.request.user.pk))
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
        context['profile'] = Profile.objects.get(pk=self.request.user.pk)

        return context


class RegisterApiView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        profile_data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'user': user.pk,
        }

        profile_serializer = ProfileSerializer(data=profile_data)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)


class LoginApiView(token_views.ObtainAuthToken):  # Login view in REST only project
    permission_classes = [permissions.AllowAny]


class UserApiUpdateView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        instance = serializer.save()

        # Update the associated profile
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile_data = self.request.data.get('profile', {})
        profile_serializer = ProfileSerializer(profile, data=profile_data, partial=True)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()


class UserApiDeleteView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProfileApiUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        profile_data = self.request.data.get('profile', {})
        profile_serializer = ProfileSerializer(instance=instance, data=profile_data, partial=True)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
