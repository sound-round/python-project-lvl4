from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status


class Tag(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    executor = models.ForeignKey(
        User, related_name='executor', on_delete=models.CASCADE, null=True
    )
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE, null=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Tasks"
