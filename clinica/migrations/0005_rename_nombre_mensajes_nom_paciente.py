# Generated by Django 4.2.6 on 2023-10-30 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_mensajes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='nombre',
            new_name='nom_paciente',
        ),
    ]
