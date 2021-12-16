from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    labels = models.ManyToManyField(Label, related_name='labels', blank=True)
    executor = models.ForeignKey(
        User, related_name='executor',
        on_delete=models.PROTECT, blank=True, null=True,
    )
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.PROTECT, null=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Tasks"
