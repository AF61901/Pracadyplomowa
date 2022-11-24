from django import forms
from .models import MyUser, Pacjenci, Lekarze, TITLE_CHOICES, SPECIALIZATION_CHOICES
from django.forms import TextInput
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from localflavor.pl.forms import PLPostalCodeField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Row, Column




class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    imie = forms.CharField(label='Imię')
    nazwisko = forms.CharField()
    telefon = PhoneNumberField(widget=TextInput(attrs={'type':'number'}))
    PESEL = forms.CharField(label='PESEL', widget=TextInput(attrs={'type':'number'}))
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'email', 
        'password1', 
        'password2',
            Row(
                Column('imie', css_class='form-group col-md-6 mb-0'),
                Column('nazwisko', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'telefon',
            'PESEL',
            Row(
                Column('kod_pocztowy', css_class='form-group col-md-2 mb-0'),
                Column('miejscowosc', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ulica', css_class='form-group col-md-6 mb-0'),
                Column('numer_domu', css_class='form-group col-md-3 mb-0'),
                Column('numer_lokalu', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            
        )

    

class DoctorRegisterForm(UserCreationForm):
    image = forms.ImageField(label='Zdjęcie', required=False)
    imie = forms.CharField(label='Imię')
    nazwisko = forms.CharField()
    telefon = PhoneNumberField(widget=TextInput(attrs={'type':'number'}))
    tytul = forms.ChoiceField(label='Tytuł', choices=TITLE_CHOICES)
    specjalizacja = forms.ChoiceField(choices=SPECIALIZATION_CHOICES)

    class Meta:
        model = Lekarze
        MyUser.is_doctor
        fields = ['email', 
        'password1', 
        'password2', 
        'imie', 
        'nazwisko',
        'telefon',
        'tytul', 
        'specjalizacja', 
        'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'email', 
        'password1', 
        'password2',
            Row(
                Column('imie', css_class='form-group col-md-6 mb-0'),
                Column('nazwisko', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'telefon',
            Row(
                Column('tytul', css_class='form-group col-md-2 mb-0'),
                Column('specjalizacja', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'image',
        )

    def save(self, commit=True):
        user = super(DoctorRegisterForm, self).save(commit=False)
        user.user_type = "L"
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Pacjenci
        fields = ['email', 
        'telefon',
        'kod_pocztowy',
        'miejscowosc',
        'ulica',
        'numer_domu',
        'numer_lokalu']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'email', 
            'telefon',
            Row(
                Column('kod_pocztowy', css_class='form-group col-md-3 mb-0'),
                Column('miejscowosc', css_class='form-group col-md-9 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ulica', css_class='form-group col-md-6 mb-0'),
                Column('numer_domu', css_class='form-group col-md-3 mb-0'),
                Column('numer_lokalu', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            )
        )

class DoctorUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Lekarze
        fields = ['email', 
        'telefon',
        ]