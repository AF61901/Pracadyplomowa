# Generated by Django 4.0.6 on 2022-11-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_myuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='data_urodzenia',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='gmina',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='plec',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='powiat',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='wojewodztwo',
        ),
        migrations.AddField(
            model_name='myuser',
            name='numer_lokalu',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Numer lokalu'),
        ),
    ]
