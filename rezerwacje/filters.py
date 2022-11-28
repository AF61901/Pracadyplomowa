import django_filters
from django_filters.widgets import RangeWidget
from .forms import DateInput

from .models import Lekarze, Rezerwacje


class UmowFilter(django_filters.FilterSet):
  
    class Meta:
        model = Lekarze
        fields = ['specjalizacja', 'imie', 'nazwisko']

class RezerwFilter(django_filters.FilterSet):
    data = django_filters.DateFromToRangeFilter(label='Data', widget=RangeWidget(attrs={'type': 'date'}))
    order_date = django_filters.OrderingFilter(
        choices=(
            ('data', ('Data (Rosnąco)')),
            ('-data', ('Data (Malejąco)'))
        ),
        fields = (
            'data', 'data'
        ),
        empty_label = None,
        null_label = None
    )
    class Meta:
        model = Rezerwacje
        fields = ['lekarz', 'pacjent']

class RezerwlFilter(django_filters.FilterSet):
    data = django_filters.DateFromToRangeFilter(label='Data', widget=RangeWidget(attrs={'type': 'date'}))
    order_date = django_filters.OrderingFilter(
        choices=(
            ('data', ('Data (Rosnąco)')),
            ('-data', ('Data (Malejąco)'))
        ),
        fields = (
            'data', 'data'
        ),
        empty_label = None,
        null_label = None
    )
    class Meta:
        model = Rezerwacje
        fields = ['lekarz']

class RezerwpFilter(django_filters.FilterSet):
    data = django_filters.DateFromToRangeFilter(label='Data', widget=RangeWidget(attrs={'type': 'date'}))
    order_date = django_filters.OrderingFilter(
        choices=(
            ('data', ('Data (Rosnąco)')),
            ('-data', ('Data (Malejąco)'))
        ),
        fields = (
            'data', 'data'
        ),
        empty_label = None,
        null_label = None
    )
    class Meta:
        model = Rezerwacje
        fields = ['pacjent']