from django.db import models

from users.models import TITLE_CHOICES, Lekarze, Pacjenci
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

TIMESLOT_LIST = (
        (0, '08:00'),
        (1, '08:30'),
        (2, '09:00'),
        (3, '09:30'),
        (4, '10:00'),
        (5, '10:30 '),
        (6, '11:00 '),
        (7, '11:30 '),
        (8, '12:00 '),
        (9, '12:30 '),
        (10, '13:00 '),
        (11, '13:30 '),
        (12, '14:00 '),
        (13, '14:30 '),
        (14, '15:00 '),
        (15, '15:30 '),
    )

class Rezerwacje(models.Model):

    class Meta:
        unique_together = ('lekarz', 'data', 'godzina')
        verbose_name_plural = 'Rezerwacje'


    lekarz = models.ForeignKey(Lekarze,on_delete = models.CASCADE)
    pacjent = models.ForeignKey(Pacjenci,on_delete = models.CASCADE)
    data = models.DateField()
    godzina = models.IntegerField(choices=TIMESLOT_LIST)

    

    def __str__(self):
        return '{} {} Lekarz: {} {} Pacjent: {}'.format(self.data, self.time, self.lekarz.tytul, self.fullname_l, self.fullname_p)

    @property
    def time(self):
        return TIMESLOT_LIST[self.godzina][1]
  

    @property
    def fullname_l(self):
        return ' %s %s' % (self.lekarz.imie, self.lekarz.nazwisko)
    
    @property
    def fullname_p(self):
        return '%s %s %s' % (self.pacjent.imie, self.pacjent.nazwisko, self.pacjent.PESEL)

    @property
    def wtoku(self):
     return date.today() < self.data


class Kontakt(models.Model):

    class Meta:
        verbose_name_plural = 'Kontakt'

    imieinazwisko = models.CharField(('Imie i nazwisko'),max_length=50)
    email = models.EmailField(('Adres email'))
    telefon = PhoneNumberField(('Telefon'))
    tytul = models.CharField(('Tytuł wiadomości'), max_length=250)
    wiadomosc = models.TextField(('Treść wiadomości'))
    submit_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return '{} Tytuł: {}'.format(self.email, self.tytul)