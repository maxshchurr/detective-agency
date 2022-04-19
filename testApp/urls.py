from django.urls import path
from . import views


urlpatterns = [

    path('client-reg/', views.client_registration, name='client-registration'),

]

