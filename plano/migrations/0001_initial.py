# Generated by Django 3.1.1 on 2021-01-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configurations', '0009_ordemservico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.FloatField()),
                ('dia_util', models.BooleanField()),
                ('feriado', models.BooleanField()),
                ('duracao_feriado', models.FloatField()),
                ('suspenso', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Justificativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NivelAvaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrdemAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=1000)),
                ('pacto_minimo_reducao', models.IntegerField()),
                ('inativo', models.BooleanField()),
                ('descricao_link', models.CharField(max_length=300)),
                ('id_grupo_atividade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdemGrupoAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('inativo', models.BooleanField()),
                ('grupo_atividade_original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.grupoatividade')),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.ordemservico')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemTipoAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faixa', models.CharField(max_length=100)),
                ('duracao_faixa', models.FloatField()),
                ('duracao_faixa_presencial', models.FloatField()),
                ('id_atividade', models.IntegerField()),
                ('texto_explicativo', models.TextField(max_length=500)),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordematividade')),
            ],
        ),
        migrations.CreateModel(
            name='Pacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_usuario', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('cpf_dirigente', models.CharField(max_length=200)),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.ordemservico')),
                ('tipo_pacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.tipopacto')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField()),
                ('quantidade_produto', models.IntegerField()),
                ('carga_horaria_produto', models.FloatField()),
                ('observacoes', models.CharField(max_length=200)),
                ('observacoes_adicionais', models.CharField(max_length=200)),
                ('motivo', models.CharField(max_length=200)),
                ('avaliacao', models.IntegerField()),
                ('entregue_no_prazo', models.BooleanField()),
                ('data_termino_real', models.DateField()),
                ('Justificativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.justificativa')),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordematividade')),
                ('grupo_atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordemgrupoatividade')),
                ('pacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.pacto')),
                ('tipo_atividade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordemtipoatividade')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemItemAvaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=500)),
                ('impacto_nota', models.FloatField()),
                ('criterio_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.criterioavaliacao')),
                ('nota_maxima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.notaavaliacao')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemCriterioAvaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('texto_explicativo', models.TextField(max_length=1000)),
                ('inativo', models.BooleanField()),
                ('avaliacao_original', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.criterioavaliacao')),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configurations.ordemservico')),
            ],
        ),
        migrations.AddField(
            model_name='ordematividade',
            name='ordem_grupo_atividade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordemgrupoatividade'),
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('pacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.pacto')),
            ],
        ),
        migrations.CreateModel(
            name='AvaliacaoProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_avaliador', models.CharField(max_length=11)),
                ('data_avaliacao', models.DateField()),
                ('quantidade_produtos_avaliados', models.IntegerField()),
                ('avaliacao', models.IntegerField()),
                ('entregue_no_prazo', models.BooleanField()),
                ('localizacao_produto', models.CharField(blank=True, max_length=200)),
                ('data_termino_real', models.DateField(blank=True)),
                ('tipo_avaliacao', models.IntegerField()),
                ('nota_final_avaliacao_detalhada', models.FloatField(blank=True)),
                ('justificativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.justificativa')),
                ('nivel_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.nivelavaliacao')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.produto')),
            ],
        ),
        migrations.CreateModel(
            name='AvaliacaoDetalhadaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.avaliacaoproduto')),
                ('ordem_criterio_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordemcriterioavaliacao')),
                ('ordem_item_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plano.ordemitemavaliacao')),
            ],
        ),
    ]
