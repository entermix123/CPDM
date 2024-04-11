from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from CPDM.accounts.models import Profile

UserModel = get_user_model()


class AccountUserCreationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountUserCreationForm, self).__init__(*args, **kwargs)
        # Set email field
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        # Set password1 field
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        # Set password2 field
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['password2'].help_text = 'Confirm your password'
        self.fields['password2'].help_text = ''

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel  # set model of the form as app UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):  # overwrite save() method to create profile
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()

        return user


class AccountUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)


class AccountLoginForm(auth_forms.AuthenticationForm):

    username = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autofocus': True}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'         # Change the field label
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Email'})                   # Add placeholder
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'})

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password."
        ),
        "inactive": _("This account is inactive."),
    }

    def clean_username(self):
        # Normalize the email address by lowercasing the domain part
        return self.cleaned_data['username'].lower()

    # def clean(self):
    #
    #     email = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #
    #     if email is not None and password:
    #         self.user_cache = authenticate(self.request, username=email, password=password)
    #         if self.user_cache is None:
    #             raise forms.ValidationError(
    #                 self.error_messages['invalid_login'],
    #                 code='invalid_login',
    #                 params={'username': self.username_field.verbose_name},
    #             )
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #
    #     return self.cleaned_data
