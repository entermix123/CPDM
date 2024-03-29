from django.core.validators import MinLengthValidator
from django.db import models

from CPDM.accounts.models import Profile
from CPDM.mixins.model_mixins import CreatedUpdatedMixin


class Company(CreatedUpdatedMixin, models.Model):
    class CompanyType(models.TextChoices):  # TODO: pre-modify structures for company types
        SERVICE = 'SERVICE',
        PRODUCTION = 'PRODUCTION',
        OTHER = 'OTHER',

    MAX_NAME_LENGTH = 15
    MIN_NAME_LENGTH = 3

    MAX_TYPE_LENGTH = 10

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=CompanyType.choices,
        default=CompanyType.OTHER,
        verbose_name="Company Type"
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_NAME_LENGTH,
                message=f'Cannot have less than {MIN_NAME_LENGTH} characters'
            ),
        ],
        unique=True,
        error_messages={'unique': 'Company with this name already exists. Choose another one'},
        help_text="Field is required",
        blank=False,
        null=False,
    )

    founded_date = models.DateField(
        auto_now_add=True,
    )

    industry = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    website = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='companies',
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    MAX_LENGTH_NAME = 45
    MIN_LENGTH_NAME = 2

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[
            MinLengthValidator(
                MIN_LENGTH_NAME,
                message=f"Location name cannot have less than {MIN_LENGTH_NAME} characters."
                        f" Try to add continent, country and city"
            )
        ],
        blank=False,
        null=False,
    )

    latitude = models.FloatField(
        blank=True,
        null=True,
    )

    longitude = models.FloatField(
        blank=True,
        null=True,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='locations',
    )
