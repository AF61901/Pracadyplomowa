from django.urls import path

from .views import (
    MojeListView,
    WizytyListView,
    UmowListView,
    WiadomosciDeleteView,
    MojeDeleteView,
    WizytyDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='rezerwacje-home'),
    path('onas/', views.onas, name='rezerwacje-onas'),
    path('kontakt/', views.kontakt, name='rezerwacje-kontakt'),
    path('lekarze/', views.lekarze, name='rezerwacje-lekarze'),
    path('umow/', UmowListView.as_view(), name='rezerwacje-umow'),
    path('<int:id>/rezerwuj/', views.new_rezerwacja, name='rezerwacje-rezerwuj'),
    path('moje/', MojeListView.as_view(), name='rezerwacje-moje'),
    path('moje/<pk>/remove/', MojeDeleteView.as_view(), name='usun_moje'),
    path('wizyty/', WizytyListView.as_view(), name='rezerwacje-wizyty'),
    path('wizyty/<pk>/remove/', WizytyDeleteView.as_view(), name='usun_wizyty'),
    path('rezerwacje/', views.wszrezerw, name='rezerwacje-rezerwacje'),
    path('wiadomosci/', views.wiadomosci, name='rezerwacje-wiadomosci'),
    path('wiadomosci/<pk>/remove/', WiadomosciDeleteView.as_view(), name='usun_wiadomosc'),
    
]
