from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models

from CPDM.accounts.managers import AccountUserManager
from CPDM.mixins.model_mixins import CreatedUpdatedMixin


# Auth data in this model
class AccountsUser(CreatedUpdatedMixin, auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "email"        # SET EMAIL AS CREDENTIALS

    objects = AccountUserManager()

    slug = models.SlugField(
        editable=False,
    )

    def save(self, *args, **kwargs):  # overwrite save() to generate and create unique slug
        self.slug = slugify(f'{self.email} + {self.created}')
        return super().save(*args, **kwargs)


class Profile(CreatedUpdatedMixin, models.Model):

    MAX_FIRST_NAME_LENGTH = 15
    MIN_FIRST_NAME_LENGTH = 3

    MAX_LAST_NAME_LENGTH = 15
    MIN_LAST_NAME_LENGTH = 3

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_FIRST_NAME_LENGTH,
                message=f'Cannot have less than {MIN_FIRST_NAME_LENGTH} characters'
            ),
        ],
        help_text="Field is required",
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LAST_NAME_LENGTH,
                message=f'Cannot have less than {MIN_LAST_NAME_LENGTH} characters'
            ),
        ],
        help_text="Field is required",
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AccountsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )   # we can access profile_obj.pk and also true profile_obj.user_id

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.user.email
