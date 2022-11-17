from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, DoctorRegisterForm, UserUpdateForm, DoctorUpdateForm

def rejestruj(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('imie')
            messages.success(request, f'Konto zostało utworzone dla {username}!')
            return redirect('loguj')
    else:
        form = UserRegisterForm()
    return render(request, 'users/rejestruj.html', {'form': form})

@login_required
def konto(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user.pacjenci)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Konto zostało zaktualizowane!')
            return redirect('konto')

    else:
        u_form = UserUpdateForm(instance = request.user.pacjenci)


    context = {
        'u_form': u_form
    }

    return render(request, 'users/konto.html', context)

@login_required
def kontol(request):
    if request.method == 'POST':
        p_form = DoctorUpdateForm(request.POST, instance = request.user.lekarze)
        if p_form.is_valid:
            p_form.save()
            messages.success(request, f'Konto zostało zaktualizowane!')
            return redirect('kontol')

    else:
        p_form = DoctorUpdateForm(instance = request.user.lekarze)


    context = {
        'p_form': p_form
    }

    return render(request, 'users/kontol.html', context)

@login_required
def dodaj(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rezerwacje-home')
    else:
        form = DoctorRegisterForm()
    return render(request, 'users/dodajlekarza.html', {'form': form})