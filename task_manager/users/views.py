# from django.shortcuts import render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


class UsersList(ListView):

    model = User
    template_name = "users/list.html"
    context_object_name = 'users_list'
    # paginate_by = 15


class UserCreate(CreateView):

    model = User
    fields = ['username', 'first_name', 'last_name', 'password']
    template_name = "users/user_form.html"

    def get_success_url(self):
        return reverse('index')

