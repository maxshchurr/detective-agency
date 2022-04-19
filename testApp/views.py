from django.http import HttpResponse
from . models import *
from django.shortcuts import render, redirect

from .forms import ClientRegistrationForm

# РЕГИСТРАЦИЯ НОВОГО КЛИЕНТА(ПОКА БЕЗ ПРОВЕРОК)

def client_registration(request):
    ctx = {}
    if request.POST:
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            # Обращение к форме -> cleaned_data['full_name'](и остальные) это поля
            # full_name(и остальные) в ClientRegistrationForm
            cleaned_data = form.cleaned_data
            full_name = cleaned_data['full_name']
            email = cleaned_data['email']
            client_login = cleaned_data['client_login']
            client_password = cleaned_data['client_password']
            tel_number = cleaned_data['tel_number']

            # Создание сущности клиент -> full_name(поле в БД)=full_name(поле в ClientRegistrationForm)
            new_client = Clients(
                full_name=full_name,
                email=email,
                client_login=client_login,
                client_password=client_password,
                tel_number=tel_number
            )

            new_client.save()

            # login(request, new_client)
            return HttpResponse("Success!Signed up")
        else:
            ctx['registration_form'] = form
    else:
        form = ClientRegistrationForm()
        ctx['registration_form'] = form
    return render(request, 'registration_form.html', ctx)



