from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.accounts.models import Profile
from CPDM.mixins.model_mixins import CreatedUpdatedMixin


UserModel = get_user_model()


class Activity(CreatedUpdatedMixin, models.Model):
    MAX_LENGTH_TITLE = 25
    MIN_LENGTH_TITLE = 5

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        validators=[
            MinLengthValidator(
                MIN_LENGTH_TITLE,
                message=f'Cannot have less than {MIN_LENGTH_TITLE} characters'
            ),
        ],
        unique=True,
        error_messages={'unique': 'Activity with this title already exists, Include department name in the title.\
         Example: "title"-"Department name"'},
        help_text="Field is required.",
        blank=False,
        null=False,
    )

    description = models.TextField(
        help_text='Field is required. Enter a brief description of the activity',
        blank=False,
        null=False,
    )

    owner = models.ForeignKey(
        UserModel,
        related_name='activities',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
