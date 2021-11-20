from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import validate_password
# from django.core import validators


class UserCreateForm(UserCreationForm):

    first_name = forms.CharField(
        label=_(u'First name'), max_length=30, required=False,
    )
    last_name = forms.CharField(
        label=_(u'Last name'), max_length=30, required=False,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]


class UserUpdateForm(UserChangeForm):

    first_name = forms.CharField(
        label=_(u'First name'), max_length=30, required=False,
    )
    last_name = forms.CharField(
        label=_(u'Last name'), max_length=30, required=False,
    )
    password = forms.CharField(
        label=_(u'Password'),
        max_length=30,
        required=False,
        widget=forms.PasswordInput(),
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]
