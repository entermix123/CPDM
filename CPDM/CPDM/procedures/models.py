from django.contrib.auth import get_user_model
from django.db import models

from CPDM.mixins.model_mixins import CreatedUpdatedMixin
from CPDM.processes.models import Process


UserModel = get_user_model()


class Procedure(CreatedUpdatedMixin, models.Model):

    MAX_NAME_LENGTH = 16

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    # TODO relation - join table with processes and procedure tasks
    process = models.ForeignKey(
        Process,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="processes"
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ProcedureTask(CreatedUpdatedMixin, models.Model):

    description = models.TextField(
        blank=False,
        null=False,
        default='Add description'
    )

    duration_days = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=3
    )


class RelationProcedureTaskTask(CreatedUpdatedMixin, models.Model):

    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
    )

    task = models.ForeignKey(
        ProcedureTask,
        on_delete=models.CASCADE,
    )
