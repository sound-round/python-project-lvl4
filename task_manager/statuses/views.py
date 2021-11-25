# from django.http import request
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.db.models import ProtectedError¶
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm


class StatusesList(ListView):

    model = Status
    template_name = "statuses/list.html"
    context_object_name = 'statuses_list'


class StatusCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    login_url = '/login/'
    form_class = StatusForm
    template_name = "create_form.html"
    success_message = _("Status was created successfully.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Create status"
        context['button_name'] = "Create"
        return context

    def get_success_url(self):
        return reverse('statuses-list')


class StatusUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    login_url = '/login/'
    model = Status
    form_class = StatusForm
    template_name = "update_form.html"
    success_message = _("Status was updated successfully.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Update status"
        context['button_name'] = "Update"
        return context

    def get_success_url(self):
        return reverse('statuses-list')


class StatusDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    login_url = '/login/'
    model = Status
    template_name = "confirm_delete.html"
    success_message = _("Status was deleted successfully.")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StatusDelete, self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError¶:
            error_message = _(
                'Not possible to delete the status because it is being used.'
            )
            messages.error(self.request, error_message)
            return reverse('statuses-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Delete status"
        context['button_name'] = "Confirm"
        context['back_button'] = "Back"
        return context

    def get_success_url(self):
        return reverse('statuses-list')
