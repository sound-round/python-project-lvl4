from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import ugettext as _
import django_filters


class Task(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    labels = models.ManyToManyField(
        Label, related_name='labels',
        through='Labeling',
        through_fields=('task', 'label'),
        blank=True,
    )
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


class Labeling(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)


class TaskFilter(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        field_name='status',
        queryset=Status.objects.all(),
        label=_("Status"),
    )
    executor = labels = django_filters.ModelChoiceFilter(
        field_name='executor',
        queryset=User.objects.all(),
        label=_("Executor"),
    )
    labels = django_filters.ModelChoiceFilter(
        field_name='labels',
        queryset=Label.objects.all(),
        label=_("Label"),
    )

    @property
    def qs(self):
        tasks = super().qs

        if self.request.GET.get('self_tasks', None):
            executor = self.request.user.id
            return tasks.filter(executor=executor)
        return tasks
