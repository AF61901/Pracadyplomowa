from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

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
    return render(request, 'users/konto.html')