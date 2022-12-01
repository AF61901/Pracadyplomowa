from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, DoctorRegisterForm, UserUpdateForm, DoctorUpdateForm

def rejestruj(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(request, f'Konto zostało utworzone dla {username}!')
            return redirect('loguj')
    else:
        form = UserRegisterForm()
    return render(request, 'users/rejestruj.html', {'form': form})

@login_required
def konto(request):
    if request.user.user_type == 'P':
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
    else:
        return redirect('/')

@login_required
def kontol(request):
    if request.user.user_type == 'L':
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
    else:
        return redirect('/')

@login_required
def dodaj(request):
    if request.user.user_type == 'M':
        if request.method == 'POST':
            form = DoctorRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('rezerwacje-home')
        else:
            form = DoctorRegisterForm()
        return render(request, 'users/dodajlekarza.html', {'form': form})
    else:
        return redirect('/')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Twoje hasło zostało zmienione')
            if request.user.user_type == "P":
                return redirect('konto')
            elif request.user.user_type == "L":
                return redirect('kontol')
        else:
            messages.error(request, 'Popraw poniższe błędy')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })