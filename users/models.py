from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator


class MyUser(AbstractUser):
    username = None
    type_choices = (
        ('M', 'Moderator'),
        ('L', 'Lekarz'),
        ('P', 'Pacjent')
    )
    user_type = models.CharField('Typ', max_length=1, choices=type_choices, default='P')
    email = models.EmailField(('Adres email'), unique=True)
    imie = models.CharField(('Imię'), max_length = 25, blank=True, null=True)
    nazwisko = models.CharField(('Nazwisko'), max_length = 50, blank=True, null=True)
    telefon = PhoneNumberField(('Telefon'), unique=True, blank=True, null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def is_patient(self):

        return self.user_type == 'P'

    def is_doctor(self):

        return self.user_type == 'L'

    def is_moderator(self):

        return self.user_type == 'M'


class LekarzManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='L')


class PacjentManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='P')

class ModeratorManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='M')

class Pacjenci(MyUser):
    username = None

    image = models.ImageField(default='default.jpg', upload_to='konto_pics')
    PESEL = models.CharField(max_length=11, validators=[MinLengthValidator(11)], unique=True, blank=True, null=True)
    kod_pocztowy = models.CharField(('Kod pocztowy'),max_length=30, blank=True, null=True)
    miejscowosc = models.CharField(('Miejscowość'), max_length=30, blank=True, null=True)
    ulica = models.CharField(('Ulica'),max_length=30, blank=True, null=True)
    numer_domu = models.CharField(('Numer domu'),max_length=10, blank=True, null=True)
    numer_lokalu = models.CharField(('Numer lokalu'),max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.fullname_p

    @property
    def fullname_p(self):
        return '%s %s %s' % (self.imie, self.nazwisko, self.PESEL)

    class Meta:
        ordering = ['imie', 'nazwisko']
        verbose_name_plural = 'Pacjenci'


SPECIALIZATION_CHOICES = (
        ("1", "Lekarz rodzinny"),
        ("2", "Ortopedia"),
        ("3", "Stomatologia"),
        ("4", "Kardiologia"),
        ("5", "Ginekologia"),
        ("6", "Neurologia"),
        ("7", "Dermatologia"),
        ("8", "Okulistyka"),
        ("9", "Urologia")
    )

TITLE_CHOICES = (
        ("lek.", "lek."),
        ("lek. dent.", "lek. dent."),
        ("dr n. med.", "dr n. med."),
        ("dr hab n. med.", "dr hab n. med."),
        ("prof. dr hab", "prof. dr hab"),
    )

class Lekarze(MyUser):
    
    

    username = None

    image = models.ImageField(default='docdef.jpg', upload_to='konto_pics')
    specjalizacja = models.CharField(('Specjalizacja'), max_length=50, choices=SPECIALIZATION_CHOICES, blank=True, null=True)
    tytul = models.CharField(('Tytuł'), max_length=15, choices=TITLE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return '{} {}'.format(self.tytul, self.fullname_l)

    @property
    def fullname_l(self):
        return ' %s %s' % (self.imie, self.nazwisko)
    

    class Meta:
        ordering = ['specjalizacja', 'nazwisko']
        verbose_name_plural = 'Lekarze'
    
    
    
    

  
