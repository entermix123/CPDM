from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.activities.models import Activity
from CPDM.company.models import Company
from CPDM.mixins.model_mixins import CreatedUpdatedMixin
from CPDM.processes.models import Process

UserModel = get_user_model()


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

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='departments',
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='departments'
    )

    activities = models.ManyToManyField(
        Activity,
        blank=True,
        null=True,
        related_name='departments_in_activity'
    )

    processes = models.ManyToManyField(
        Process,
        blank=True,
        null=True,
        related_name='departments_in_process'
    )

    def __str__(self):
        return self.name
