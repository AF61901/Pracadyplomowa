from django import forms
from .models import Pacjenci
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from localflavor.pl.forms import PLPostalCodeField



class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    imie = forms.CharField(label='Imię')
    nazwisko = forms.CharField()
    telefon = PhoneNumberField(widget=TextInput(attrs={'type':'number'}))
    PESEL = forms.CharField(widget=TextInput(attrs={'type':'number'}))
    kod_pocztowy = PLPostalCodeField()
    miejscowosc = forms.CharField(label='Miejscowość')
    ulica = forms.CharField()
    numer_domu = forms.CharField()
    numer_lokalu = forms.CharField(required=False)

    class Meta:
        model = Pacjenci
        fields = ['email', 
        'password1', 
        'password2', 
        'imie', 
        'nazwisko', 
        'telefon', 
        'PESEL', 
        'kod_pocztowy',
        'miejscowosc',
        'ulica',
        'numer_domu',
        'numer_lokalu']