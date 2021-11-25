from django.contrib import admin
from task_manager.tasks.models import Task, Tag


admin.site.register(Task)
admin.site.register(Tag)
