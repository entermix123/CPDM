from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.company.models import Company
from CPDM.departments.models import Department
from CPDM.employees.validators import validate_employee_first_name, validate_employee_last_name


UserModel = get_user_model()


class Employee(models.Model):
    MAX_FIRST_NAME_LENGTH = 15
    MIN_FIRST_NAME_LENGTH = 3

    MAX_LAST_NAME_LENGTH = 15
    MIN_LAST_NAME_LENGTH = 3

    MAX_TITLE_LENGTH = 30
    MIN_TITLE_LENGTH = 3

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_FIRST_NAME_LENGTH,
                message=f'First Name must be at least {MAX_FIRST_NAME_LENGTH} characters long'
            ),
            validate_employee_first_name,
        ],
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LAST_NAME_LENGTH,
                message=f'First Name must be at least {MAX_LAST_NAME_LENGTH} characters long'
            ),
            validate_employee_last_name,
        ],
    )

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_TITLE_LENGTH,
                message=f'Title must be at least {MIN_TITLE_LENGTH} characters long'
            ),
        ],
        blank=True,
        null=True,
        help_text="Enter seniority and position"
    )

    salary = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    department = models.ManyToManyField(
        Department,
        related_name='employees_departments',
        blank=True,
        null=True,
    )

    company = models.ManyToManyField(
        Company,
        related_name='employees_companies',
        blank=True,
        null=True,
    )

    company_owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
