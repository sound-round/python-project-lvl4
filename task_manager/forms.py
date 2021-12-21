from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.password_validation import validate_password


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(
        label=_('Username'), max_length=30, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            }),
    )

    password = forms.CharField(
        label=_('Password'),
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password',
            }),
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
