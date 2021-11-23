from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import ugettext as _


def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, f"{_('Welcome to task-manager')}, {username}!"
                )
            return redirect('index')
        else:
            messages.error(request, _('Wrong username or password.'))
    return render(request, 'login_form.html')


def user_logout(request):
    logout(request)
    return redirect('index')
