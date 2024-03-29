from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify

from CPDM.mixins.model_mixins import CreatedUpdatedMixin
from CPDM.validators.accounts_validators import validate_username


class Profile(CreatedUpdatedMixin, models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2

    MAX_FIRST_NAME_LENGTH = 15
    MIN_FIRST_NAME_LENGTH = 3

    MAX_LAST_NAME_LENGTH = 15
    MIN_LAST_NAME_LENGTH = 3

    MAX_PASSWORD_LENGTH = 30
    MIN_PASSWORD_LENGTH = 6

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_USERNAME_LENGTH,
                message=f'Cannot have less than {MIN_USERNAME_LENGTH} characters'
            ),
            validate_username,
        ],
        unique=True,
        error_messages={'unique': 'Username already exists. Please choose a different one'},
        help_text=f"Field is required.\nEnsure username contains only letters, numbers, and underscores.",
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_FIRST_NAME_LENGTH,
                message=f'Cannot have less than {MIN_FIRST_NAME_LENGTH} characters'
            ),
        ],
        help_text="Field is required",
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LAST_NAME_LENGTH,
                message=f'Cannot have less than {MIN_PASSWORD_LENGTH} characters'
            ),
        ],
        help_text="Field is required",
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_PASSWORD_LENGTH,
                message=f'Cannot have less than {MIN_PASSWORD_LENGTH} characters'
            ),

        ],
        help_text=f"Field is required. Password must be at least {MIN_PASSWORD_LENGTH} characters long.\n\
         Password must contain at least 2 special characters, one capital letter."
    )

    email = models.EmailField(
        help_text="Field is required",
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        editable=False,
    )

    def save(self, *args, **kwargs):  # overwrite save() to generate and create unique slug
        self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
