# Generated by Django 4.0.6 on 2022-11-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lekarze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('imieinazwisko', models.CharField(blank=True, max_length=100, null=True, verbose_name='Imię i nazwisko')),
                ('specjalność', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]