from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
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
        self.fields['password2'].help_text = ''

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):
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
        self.fields['username'].label = 'Email'
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Email'})
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
