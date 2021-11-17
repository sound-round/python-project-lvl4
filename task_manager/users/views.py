from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User


class UsersList(ListView):

    model = User
    template_name = "users/list.html"
    context_object_name = 'users_list'
    # paginate_by = 15
