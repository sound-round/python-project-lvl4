# from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from task_manager.users.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


class UsersList(ListView):

    model = User
    template_name = "users/list.html"
    context_object_name = 'users_list'
    # TODO paginate_by = 15


class UserCreate(CreateView):

    form_class = UserCreateForm
    template_name = "users/user_create_form.html"

    def get_success_url(self):
        return reverse('user-login')


# @login_required(login_url='login')
class UserUpdate(UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = "users/user_update_form.html"

    def get_success_url(self):
        return reverse('users-list')


# @login_required(login_url='login')
class UserDelete(DeleteView):

    model = User
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy('users-list')
