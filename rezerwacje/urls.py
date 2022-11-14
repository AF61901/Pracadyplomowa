from django.urls import path

from .views import (
    MojeListView,
    WizytyListView,
    UmowListView
)
from . import views

urlpatterns = [
    path('', views.home, name='rezerwacje-home'),
    path('onas/', views.onas, name='rezerwacje-onas'),
    path('lekarze/', views.lekarze, name='rezerwacje-lekarze'),
    path('umow/', UmowListView.as_view(), name='rezerwacje-umow'),
    path('<int:id>/rezerwuj/', views.new_rezerwacja, name='rezerwacje-rezerwuj'),
    path('moje/', MojeListView.as_view(), name='rezerwacje-moje'),
    path('wizyty/', WizytyListView.as_view(), name='rezerwacje-wizyty'),
]
