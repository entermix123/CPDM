from django.db import models

from CPDM.mixins.model_mixins import CreatedUpdatedMixin
from CPDM.processes.models import Process


class Procedure(CreatedUpdatedMixin, models.Model):

    # TODO: complete the class
    procedure = models.ForeignKey(
        Process, on_delete=models.DO_NOTHING,
        related_name="processes"
    )
