from django.shortcuts import render, redirect
from .models import Rezerwacje, Pacjenci, Lekarze, Kontakt
from .forms import RezerwacjeForm, KontaktForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from .filters import UmowFilter, RezerwFilter, RezerwlFilter, RezerwpFilter
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context ={
        'lekarze': Lekarze.objects.all()[2:5],
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

@login_required
def wiadomosci(request):
    if request.user.user_type == "M":
        context ={
            'Kontakt': Kontakt.objects.all().order_by('-submit_date') ,
            "title" : "Wiadomości"
        }
        return render(request, 'rezerwacje/wiadomosci.html', context)
    else:
        return redirect('/')

@login_required
def wszrezerw(request):
    rezerw_filter = RezerwFilter(request.GET, queryset=Rezerwacje.objects.all().order_by('data'))

    if request.user.user_type == "M":
        context ={
            'Rezerwacje': rezerw_filter.qs,
            'rezerw_filter': rezerw_filter.form,
            "title" : "Rezerwacje"
        }
        return render(request, 'rezerwacje/wszystkierezerwacje.html', context)
    else:
        return redirect('/')

class WiadomosciDeleteView(DeleteView):
    model = Kontakt
    success_url = reverse_lazy('rezerwacje-wiadomosci')


class MojeDeleteView(DeleteView):
    model = Rezerwacje
    success_url = reverse_lazy('rezerwacje-moje')


class WizytyDeleteView(DeleteView):
    model = Rezerwacje
    success_url = reverse_lazy('rezerwacje-wizyty')


class WizytyListView(LoginRequiredMixin, ListView):
    model = Rezerwacje
    template_name = 'rezerwacje/wizyty.html'
    context_object_name = 'Rezerwacje'


    def get_queryset(self):
        self.filterset = RezerwpFilter(self.request.GET, queryset=Rezerwacje.objects.filter(
            lekarz=self.request.user
        ).order_by('data')) 
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


class MojeListView(LoginRequiredMixin, ListView):
    model = Rezerwacje
    template_name = 'rezerwacje/mojerezerwacje.html'
    context_object_name = 'Rezerwacje'

    def get_queryset(self):
        self.filterset = RezerwlFilter(self.request.GET, queryset=Rezerwacje.objects.filter(
            pacjent=self.request.user
        ).order_by('data'))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context


    

class UmowListView(LoginRequiredMixin, ListView):
    model = Lekarze
    queryset = Lekarze.objects.all()
    template_name = 'rezerwacje/umow.html'
    context_object_name = 'Lekarze'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UmowFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context



@login_required
def new_rezerwacja(request, id=None):
    form = RezerwacjeForm(request.POST)
    desc = Lekarze.objects.get(id=id)
    
    if not request.user.is_authenticated:
        return redirect('/loguj')
    if request.user.user_type == "P":
        if form.is_valid():
            data = form.cleaned_data['data']
            godzina = form.cleaned_data['godzina']
            zamowienie = Rezerwacje(pacjent=request.user.pacjenci, lekarz=desc,
                data=data, godzina=godzina)
            is_avaible = zamowienie.check_reser()

            if data <= data.today():
                messages.warning(request, f'Data się nie zgadza')
                return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})
            elif data.isoweekday() > 5:
                messages.warning(request, f'Przychodnia pracuje w dni powszednie')
                return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})
            elif is_avaible:
                zamowienie.save()
                messages.success(request, f'Zarezerwowano termin wizyty!')
                return redirect('/moje')
            else:
                messages.warning(request, f'Termin jest już zarezerwowany')
                return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})

        else:
            form = RezerwacjeForm()
            return render(request, 'rezerwacje/rezerwuj.html', {'desc': desc,'form': form})
    else:
        return redirect('/')
