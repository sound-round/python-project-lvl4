from django.db import models
from django.utils.translation import ugettext as _


class Status(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Statuses"
