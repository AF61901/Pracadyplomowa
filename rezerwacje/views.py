from django.shortcuts import render, redirect
from .models import Rezerwacje, Pacjenci, Lekarze, Kontakt
from .forms import RezerwacjeForm, KontaktForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context ={
        'lekarze': Lekarze.objects.all()[:3],
        "title" : "Strona Główna"
    }
    return render(request, 'rezerwacje/home.html', context)

def onas(request):
    return render(request, 'rezerwacje/onas.html', {'title': 'O nas'})

def kontakt(request):
    if request.method == 'POST':
        form = KontaktForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Wysłano wiadomość!')
            return redirect('/kontakt')
            
    else:
        form = KontaktForm()
    return render(request, 'rezerwacje/kontakt.html', {'form': form, 'title': 'Kontakt'}, )

def lekarze(request):
    context ={
        'lekarze': Lekarze.objects.all(),
        "title" : "Lekarze"
    }
    return render(request, 'rezerwacje/lekarze.html', context)

def wiadomosci(request):
    context ={
        'Kontakt': Kontakt.objects.all().order_by('-submit_date') ,
        "title" : "Wiadomości"
    }
    return render(request, 'rezerwacje/wiadomosci.html', context)

class WiadomosciDeleteView(DeleteView):
    model = Kontakt
    success_url = reverse_lazy('rezerwacje-wiadomosci')

class WizytyListView(LoginRequiredMixin, ListView):
    model = Rezerwacje
    template_name = 'rezerwacje/wizyty.html'
    context_object_name = 'Rezerwacje'



    def get_queryset(self):
        return Rezerwacje.objects.filter(
            lekarz=self.request.user
        ).order_by('data')  


class MojeListView(LoginRequiredMixin, ListView):
    model = Rezerwacje
    template_name = 'rezerwacje/mojerezerwacje.html'
    context_object_name = 'Rezerwacje'


    def get_queryset(self):
        return Rezerwacje.objects.filter(
            pacjent=self.request.user
        ).order_by('data')

class UmowListView(LoginRequiredMixin, ListView):
    model = Lekarze
    template_name = 'rezerwacje/umow.html'
    context_object_name = 'Lekarze'


    def get_queryset(self):
        return Lekarze.objects.all()

@login_required
def new_rezerwacja(request, id=None):
    form = RezerwacjeForm(request.POST)
    desc = Lekarze.objects.get(id=id)
    if not request.user.is_authenticated:
        return redirect('/loguj')

    if form.is_valid():
        data = form.cleaned_data['data']
        godzina = form.cleaned_data['godzina']
        zamowienie = Rezerwacje(pacjent=request.user.pacjenci, lekarz=desc,
            data=data, godzina=godzina)

        if data <= data.today():
            messages.warning(request, f'Data się nie zgadza')
            return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})
        elif data.isoweekday() > 5:
            messages.warning(request, f'Nie w weekend')
            return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})
        else:
            zamowienie.save()
            return redirect('/moje')


    else:
        form = RezerwacjeForm()
        return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})
