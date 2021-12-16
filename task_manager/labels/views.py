# from django.http import request
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.db.models import ProtectedError
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm


class LabelsList(ListView):

    model = Label
    template_name = "labels/list.html"
    context_object_name = 'labels_list'


class LabelCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    login_url = '/login/'
    form_class = LabelForm
    template_name = "create_form.html"
    success_message = _("Label was created successfully.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Create label"
        context['button_name'] = "Create"
        return context

    def get_success_url(self):
        return reverse('labels-list')


class LabelUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    login_url = '/login/'
    model = Label
    form_class = LabelForm
    template_name = "update_form.html"
    success_message = _("Label was updated successfully.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Update label"
        context['button_name'] = "Update"
        return context

    def get_success_url(self):
        return reverse('labels-list')


class LabelDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):

    login_url = '/login/'
    model = Label
    template_name = "confirm_delete.html"
    success_message = _("Label was deleted successfully.")

    def delete(self, request, *args, **kwargs):
        super(LabelDelete, self).delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(reverse('labels-list'))

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            error_message = _(
                'Not possible to delete this label because it is being used.'
            )
            messages.error(self.request, error_message)
            return HttpResponseRedirect(reverse('labels-list'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Delete label"
        context['button_name'] = "Confirm"
        context['back_button'] = "Back"
        return context

    def get_success_url(self):
        return reverse('labels-list')
