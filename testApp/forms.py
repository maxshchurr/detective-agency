from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
import datetime
from django.http import HttpResponse

from .models import *


class EmployeesLoginForm(forms.Form):
    e_email = forms.EmailField(help_text="Enter your email address", required=True)
    password = forms.CharField(help_text='Enter your password', required=True, widget=forms.PasswordInput)


class ClientRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(label="Имя", max_length=70)
    email = forms.EmailField(label="Почта", max_length=50)
    client_login = forms.CharField(label="Логин", max_length=30)
    client_password = forms.CharField(label="Пароль", max_length=30)
    tel_number = forms.CharField(label="Телефон", max_length=13)

    class Meta:
        model = Clients
        fields = ('full_name', 'email', 'client_login', 'client_password', 'tel_number')


