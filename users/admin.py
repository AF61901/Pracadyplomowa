from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Pacjenci, Lekarze, MyUser

@admin.register(MyUser)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        (('Dane osobowe'), {'fields': ('imie', 'nazwisko',)}),

        (('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Ważne daty'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
        (('Dane osobowe'), {'fields': ('imie', 'nazwisko', 'telefon')}),
        (('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    list_display = ('email', 'imie', 'nazwisko', 'user_type', 'is_staff')
    search_fields = ('email', 'imie', 'nazwisko')
    ordering = ('email',)

@admin.register(Pacjenci)
class UserPatient(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Dane osobowe'), {'fields': ('imie', 'nazwisko', 'telefon', 'PESEL')}),
        (('Adres'), {'fields': ('kod_pocztowy', 'miejscowosc', 'ulica', 'numer_domu', 'numer_lokalu')}),
        (('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Ważne daty'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type'),
        }),
        (('Dane osobowe'), {'fields': ('imie', 'nazwisko', 'telefon', 'PESEL')}),
        (('Adres'), {'fields': ('kod_pocztowy', 'miejscowosc', 'ulica', 'numer_domu', 'numer_lokalu')}),
        (('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    list_display = ('email', 'imie', 'nazwisko', 'is_staff')
    search_fields = ('email', 'imie', 'nazwisko')
    ordering = ('email',)

@admin.register(Lekarze)
class UserDoctor(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password', 'image')}),
        (('Dane osobowe'), {'fields': ('tytul', 'imie', 'nazwisko', 'telefon', 'specjalizacja')}),
        (('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Ważne daty'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'image', 'user_type'),
        }),
        (('Dane osobowe'), {'fields': ('imie', 'nazwisko', 'telefon', 'tytul', 'specjalizacja')}),
        (('Uprawnienia'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    list_display = ('email', 'tytul', 'imie', 'nazwisko', 'specjalizacja', 'is_staff')
    search_fields = ('email', 'imie', 'nazwisko')
    ordering = ('email',)
