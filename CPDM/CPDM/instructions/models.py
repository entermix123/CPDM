from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.mixins.model_mixins import CreatedUpdatedMixin
from CPDM.procedures.models import Procedure


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


class InstructionStep(models.Model):

    class StepTypes(models.TextChoices):
        EXECUTE = 'EXECUTE',
        IF_BLOCK = 'IF_BLOCK',
        TO_PROCESS = 'TO_PROCESS',
        END_BLOCK = 'END_BLOCK'

    MAX_STEP_NAME_LENGTH = 20
    MAX_STEP_TYPE_LENGTH = 10

    number = models.PositiveIntegerField()

    instruction = models.ForeignKey(
        Instruction, on_delete=models.CASCADE,
        related_name="steps"
    )

    step_type = models.CharField(
        max_length=MAX_STEP_TYPE_LENGTH,
        choices=StepTypes.choices,
    )

    step_label = models.CharField(
        max_length=MAX_STEP_NAME_LENGTH,
    )

    step_text = models.CharField(           # OPTION FOR FAST BUILD THE INSTRUCTION
        max_length=MAX_STEP_TYPE_LENGTH,
        choices=StepTypes.choices,
    )

