from django.db import models


class CreatedUpdatedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True),
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
