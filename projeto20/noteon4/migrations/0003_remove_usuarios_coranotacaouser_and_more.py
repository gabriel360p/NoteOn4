# Generated by Django 4.1.1 on 2022-10-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteon4', '0002_usuarios_sobrenome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='CorAnotacaoUser',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='SubtituloAnotacaoUser',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='TextoAnotacaoUser',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='TituloAnotacaoUser',
        ),
    ]
