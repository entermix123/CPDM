from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.accounts.models import Profile
from CPDM.activities.models import Activity
from CPDM.mixins.model_mixins import CreatedUpdatedMixin

UserModel = get_user_model()


class Process(CreatedUpdatedMixin, models.Model):
    MAX_INSTRUCTION_NAME_LENGTH = 20
    MIN_INSTRUCTION_NAME_LENGTH = 6

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
        help_text="Enter Process description. Include Activities and Departments",
        blank=False,
        null=False,
    )

    activities = models.ManyToManyField(
        Activity,
        related_name="processes",
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="processes"
    )

    def __str__(self):
        return self.name


class ProcessStep(models.Model):
    class StepTypes(models.TextChoices):
        EXECUTE = 'EXECUTE',
        IF_BLOCK = 'IF_BLOCK',
        TO_PROCESS = 'TO_PROCESS',
        END_BLOCK = 'END_BLOCK'

    MAX_STEP_NAME_LENGTH = 20
    MAX_STEP_TYPE_LENGTH = 10

    number = models.PositiveIntegerField()

    step_type = models.CharField(
        max_length=MAX_STEP_TYPE_LENGTH,
        choices=StepTypes.choices,
    )

    step_label = models.CharField(
        max_length=MAX_STEP_NAME_LENGTH,
    )

    step_text = models.CharField(  # OPTION FOR FAST BUILD THE INSTRUCTION
        max_length=MAX_STEP_TYPE_LENGTH,
        choices=StepTypes.choices,
    )

    process = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
        related_name="steps"
    )

    def __str__(self):
        return self.step_label
