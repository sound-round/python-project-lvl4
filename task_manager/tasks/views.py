# from django.http import request
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.contrib import messages
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm


class TaskDetail(LoginRequiredMixin, DetailView):

    login_url = '/login/'
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
        context['header'] = _("Create task")
        context['button_name'] = _("Create")
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
        context['header'] = _("Update task")
        context['button_name'] = _("Update")
        return context

    def get_success_url(self):
        return reverse('tasks-list')


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    login_url = '/login/'
    model = Task
    template_name = "confirm_delete.html"
    success_message = _("Task was deleted successfully.")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.id == self.object.author.id:
            messages.success(self.request, self.success_message)
            return super(TaskDelete, self).delete(request, *args, **kwargs)
        error_message = _(
                'Not possible to delete the task '
                'because you are not the author.'
            )
        messages.error(self.request, error_message)
        return HttpResponseRedirect(reverse('tasks-list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = _("Delete task")
        context['button_name'] = _("Confirm")
        context['back_button'] = _("Back")
        return context

    def get_success_url(self):
        return reverse('tasks-list')
