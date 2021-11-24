from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm


class StatusesList(ListView):

    model = Status
    template_name = "statuses/list.html"
    context_object_name = 'statuses_list'


class StatusCreate(CreateView):

    form_class = StatusForm
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Create status"
        context['button_name'] = "Create"
        return context

    def get_success_url(self):
        return reverse('statuses-list')


class StatusUpdate(UpdateView):

    model = Status
    form_class = StatusForm
    template_name = "update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Update status"
        context['button_name'] = "Update"
        return context

    def get_success_url(self):
        return reverse('statuses-list')


class StatusDelete(DeleteView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Delete status"
        context['button_name'] = "Confirm"
        context['back_button'] = "Back"
        return context

    model = Status
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('statuses-list')
