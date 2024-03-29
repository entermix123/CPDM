from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from extend_user_model.accounts.models import Profile

UserModel = get_user_model()


class AccountUserCreationForm(auth_forms.UserCreationForm):
    age = forms.IntegerField()
    # other fields

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel                           # set model of the form as app UserModel
        fields = (UserModel.USERNAME_FIELD,)

    def save(self, commit=True):           # overwrite save() method to create profile
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            age=self.cleaned_data["age"],
        )

        if commit:
            profile.save()

        return user


class AccountUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'
