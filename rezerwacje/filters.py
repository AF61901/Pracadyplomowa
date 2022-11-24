import django_filters
from .forms import DateInput

from .models import Lekarze, Rezerwacje


class UmowFilter(django_filters.FilterSet):
  
    class Meta:
        model = Lekarze
        fields = ['specjalizacja', 'imie', 'nazwisko']

class RezerwFilter(django_filters.FilterSet):
    data = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Rezerwacje
        fields = ['lekarz', 'pacjent', 'data']

class RezerwlFilter(django_filters.FilterSet):
    data = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Rezerwacje
        fields = ['lekarz', 'data']

class RezerwpFilter(django_filters.FilterSet):
    data = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Rezerwacje
        fields = ['pacjent', 'data']