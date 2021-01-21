# Generated by Django 3.1.1 on 2021-01-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0008_auto_20210121_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=1000)),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('inativo', models.BooleanField()),
                ('criterio_avaliacoes', models.ManyToManyField(to='configurations.CriterioAvaliacao')),
                ('grupo_atividades', models.ManyToManyField(to='configurations.GrupoAtividade')),
            ],
        ),
    ]
