from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.mixins.model_mixins import CreatedUpdatedMixin
from CPDM.procedures.models import Procedure

UserModel = get_user_model()


class Instruction(CreatedUpdatedMixin, models.Model):
    MAX_INSTRUCTION_NAME_LENGTH = 40
    MIN_INSTRUCTION_NAME_LENGTH = 10

    name = models.CharField(
        max_length=MAX_INSTRUCTION_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_INSTRUCTION_NAME_LENGTH,
                message=f'Cannot have less than {MAX_INSTRUCTION_NAME_LENGTH} characters'
            ),
        ],
        blank=False,
        null=False,
    )

    description = models.TextField(
        help_text="Enter instruction description",
        blank=False,
        null=False,
    )

    procedures = models.ManyToManyField(
        Procedure,
        related_name="instructions"
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
