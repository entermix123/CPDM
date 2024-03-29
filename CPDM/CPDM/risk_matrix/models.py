from django.db import models

from CPDM.activities.models import Activity
from CPDM.company.models import Company
from CPDM.mixins.model_mixins import CreatedUpdatedMixin


class Risk(CreatedUpdatedMixin, models.Model):

    name = models.CharField(
        max_length=50,
        help_text="Field is required.",
        blank=False,
        null=False,
    )

    description = models.TextField()

    activity = models.ForeignKey(
        Activity,
        related_name='risks',
        on_delete=models.SET_NULL,
        null=True
    )

    owner = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )


class RiskLevel(models.Model):

    name = models.CharField(
        max_length=50,
    )

    value = models.IntegerField()

    risk = models.ForeignKey(
        Risk,
        on_delete=models.CASCADE,
        related_name='levels'
    )

