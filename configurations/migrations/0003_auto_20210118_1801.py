# Generated by Django 3.1.1 on 2021-01-18 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0002_perfil_unidade_usuario_usuarioperfilunidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
    ]
