from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.mixins.model_mixins import CreatedUpdatedMixin


class Department(CreatedUpdatedMixin, models.Model):
    MAX_DEPARTMENT_NAME_LENGTH = 20
    MIN_DEPARTMENT_NAME_LENGTH = 2
    name = models.CharField(
        max_length=MAX_DEPARTMENT_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_DEPARTMENT_NAME_LENGTH,
                message=f'Cannot have less than {MIN_DEPARTMENT_NAME_LENGTH} characters'
            ),
        ],
        unique=True,
        error_messages={'unique': 'Department with this name already exists. Include Department location,\
         Example: "Department name"-"Department location"'},
    )
