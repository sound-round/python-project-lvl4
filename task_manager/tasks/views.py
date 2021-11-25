# from django.http import request
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.db.models import ProtectedError
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
# from task_manager.statuses.models import Status
# from task_manager.statuses.forms import StatusForm


class TasksList(ListView):

    model = Task
    template_name = "tasks/list.html"
    context_object_name = 'tasks_list'


class TaskDetail(DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    login_url = '/login/'
    form_class = TaskForm
    template_name = "create_form.html"
    success_message = _("Task was created successfully.")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Create task"
        context['button_name'] = "Create"
        return context

    def get_success_url(self):
        return reverse('tasks-list')


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    login_url = '/login/'
    model = Task
    form_class = TaskForm
    template_name = "update_form.html"
    success_message = _("Task was updated successfully.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Update task"
        context['button_name'] = "Update"
        return context

    def get_success_url(self):
        return reverse('tasks-list')


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    login_url = '/login/'
    model = Task
    template_name = "confirm_delete.html"
    success_message = _("Task was deleted successfully.")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TaskDelete, self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            error_message = _(
                'Not possible to delete the task because it is being used.'
            )
            messages.error(self.request, error_message)
            return reverse('tasks-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Delete task"
        context['button_name'] = "Confirm"
        context['back_button'] = "Back"
        return context

    def get_success_url(self):
        return reverse('tasks-list')
