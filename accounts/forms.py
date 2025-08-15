from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from serviceBook.models import RegUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")


    class Meta:
        model = RegUser
        fields = (
            "username",
            "first_name",
            "email",
            "password1",
            "password2",
            "serviceCompany",
            "manager",
        )

