from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.company.models import Company
from CPDM.departments.models import Department
from CPDM.mixins.model_mixins import CreatedUpdatedMixin


class Software(CreatedUpdatedMixin, models.Model):

    MAX_NAME_LENGTH = 50
    MIN_NAME_LENGTH = 3

    MAX_LICENSE_NAME_LENGTH = 30
    MIN_LICENSE_NAME_LENGTH = 4

    MAX_VENDOR_URL_LENGTH = 30
    MIN_VENDOR_URL_LENGTH = 7

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_NAME_LENGTH,
                message=f'Cannot have less than {MIN_NAME_LENGTH} characters'
            )
        ],
        unique=True,
        error_messages={'unique': 'Software with this name already exists. Choose another one'},
        blank=False,
        null=False,
    )

    version = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        help_text='Field is required. Include software version'
    )

    license = models.CharField(
        max_length=MAX_LICENSE_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LICENSE_NAME_LENGTH,
                message=f'Cannot have less than {MIN_LICENSE_NAME_LENGTH} characters',
            ),
        ],
        help_text='Field is required. Include software license name and number',
        blank=False,
        null=False,
    )

    vendor = models.URLField(
        max_length=MAX_VENDOR_URL_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_VENDOR_URL_LENGTH,
                message=f'Cannot have less than {MIN_VENDOR_URL_LENGTH} characters',
            ),
        ],
        help_text='Field is required. Include software vendor URL',
        blank=False,
        null=False
    )

    departments = models.ManyToManyField(Department, related_name='software_departments')

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='software'
    )

    def __str__(self):
        return f"{self.name} {self.version}"
