from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class CreateUserForm(UserCreationForm):

    first_name = forms.CharField(label=_(u'First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_(u'Last name'), max_length=30, required=False)

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
            ]
