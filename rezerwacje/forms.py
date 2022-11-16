from datetime import date

from django import forms

from .models import Rezerwacje, Kontakt, TIMESLOT_LIST


class DateInput(forms.DateInput):
    input_type = 'date'

class RezerwacjeForm(forms.ModelForm):



    godzina = forms.ChoiceField(
        choices=TIMESLOT_LIST,
        label="Godziny przyjęć",
        widget=forms.RadioSelect,
        required=True,
         )

    class Meta:
        model = Rezerwacje
        fields = ('data', 'godzina')
        widgets = {
            'data': DateInput(),
        }

    def clean_date(self):
        day = self.cleaned_data['data']

        if day <= date.today():
            raise forms.ValidationError('Rezerwacja wymaga przynajmniej jednodniowego wyprzedzenia)', code='invalid')
        if day.isoweekday() > 5:
            raise forms.ValidationError('Data powinna być dniem roboczym)', code='invalid')

        return day  

class KontaktForm(forms.ModelForm):
    
     class Meta:
        model = Kontakt
        fields = '__all__'
        exclude = ('submit_date',)