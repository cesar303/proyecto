# Generated by Django 4.2.6 on 2023-11-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0006_paciente_visita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='numero',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dpi',
            field=models.IntegerField(max_length=13),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero',
            field=models.IntegerField(max_length=8),
        ),
    ]
