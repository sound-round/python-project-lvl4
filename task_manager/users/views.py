# from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from task_manager.users.forms import UserCreateForm, \
                                        UserUpdateForm, PasswordUpdateForm
# from django.contrib.auth.decorators import login_required


class UsersList(ListView):

    model = User
    template_name = "users/list.html"
    context_object_name = 'users_list'
    # TODO paginate_by = 15


class UserCreate(CreateView):

    form_class = UserCreateForm
    template_name = "create_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Register user"
        context['button_name'] = "Register"
        return context

    def get_success_url(self):
        return reverse('user-login')


# @login_required(login_url='login')
class UserUpdate(UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = "update_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Update user"
        context['button_name'] = "Update"
        context['page'] = "update_user"
        return context

    def get_success_url(self):
        return reverse('users-list')


# @login_required(login_url='login')
class UserDelete(DeleteView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Delete user"
        context['button_name'] = "Confirm"
        context['back_button'] = "Back"
        return context

    model = User
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('users-list')


class PasswordUpdate(PasswordChangeView):

    from_class = PasswordUpdateForm
    model = User
    template_name = "update_form.html"
    success_url = reverse_lazy('users-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = "Change password"
        context['button_name'] = "Change"
        return context
