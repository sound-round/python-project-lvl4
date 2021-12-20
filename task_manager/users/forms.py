from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import validate_password


class UserCreateForm(UserCreationForm):

    first_name = forms.CharField(
        label=_('First name'), max_length=30, required=False,
    )
    last_name = forms.CharField(
        label=_('Last name'), max_length=30, required=False,
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


class UserUpdateForm(forms.ModelForm):

    username = forms.CharField(
        label=_('Username'), max_length=30, required=False,
    )

    first_name = forms.CharField(
        label=_('First name'), max_length=30, required=False,
    )
    last_name = forms.CharField(
        label=_('Last name'), max_length=30, required=False,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]
        exclude = ('password',)


class PasswordUpdateForm(PasswordChangeForm):

    old_password = forms.CharField(
        label=_('Old password'),
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password',
            }),
        validators=[validate_password],
    )
    password1 = forms.CharField(
        label=_('New password'),
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password',
            }),
        validators=[validate_password],
    )
    password2 = forms.CharField(
        label=_('Confirm new password'),
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password',
            }),
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            'old_password',
            'password1',
            'password2',
        ]
