# Generated by Django 3.1.1 on 2021-01-28 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plano', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SituacaoPacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='pacto',
            name='carga_horaria',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='carga_horaria_total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='cpf_criador',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='cpf_solicitante',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='data_aprovacao_dirigente',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='data_interrupcao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='data_prevista_inicio',
            field=models.DateField(default='2021-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='data_prevista_termino',
            field=models.DateField(default='2021-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='data_termino_real',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='entregue_no_prazo',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='executado_no_exterior',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='justificativa_visualizacao_restrita',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='matricula_siape',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='motivo',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='possui_carga_horaria',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='processo_sei',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='status_aprovacao_dirigente',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='status_aprovacao_solicitante',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='suspensao_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='suspensao_termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='tap',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='telefone_fixo_servidor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='telefone_movel_servidor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pacto',
            name='unidade_exercicio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='visualizacao_restrita',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pacto',
            name='situacao_pacto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='plano.situacaopacto'),
            preserve_default=False,
        ),
    ]
