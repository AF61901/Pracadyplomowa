# Generated by Django 4.0.6 on 2022-11-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_myuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lekarze',
            name='tytul',
            field=models.CharField(blank=True, choices=[('lek.', 'lek.'), ('lek. dent.', 'lek. dent.'), ('dr n. med.', 'dr n. med.'), ('dr hab n. med.', 'dr hab n. med.'), ('prof. dr hab', 'prof. dr hab')], max_length=15, null=True, verbose_name='Tytuł'),
        ),
    ]
