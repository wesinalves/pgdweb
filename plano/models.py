from django.db import models
from configurations.models import OrdemServico, TipoPacto, CriterioAvaliacao, NotaAvaliacao

# Create your models here.

class Pacto(models.Model):
    cpf_usuario = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    cpf_dirigente = models.CharField(max_length=200)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete='CASCADE')
    tipo_pacto = models.ForeignKey(TipoPacto, on_delete='CASCADE')

    def __str__(self):
        return self.nome[:50] + '...'

class Historico(models.Model):
    descricao = models.CharField(max_length=200)
    pacto = models.ForeignKey(Pacto, on_delete='CASCADE')

class Cronograma(models.Model):
    data = models.DateField()
    hora = models.FloatField()
    dia_util = models.BooleanField()
    feriado = models.BooleanField()
    duracao_feriado = models.FloatField()
    suspenso = models.BooleanField()

class OrdemCriterioAvaliacao(models.Model):
    avaliacao_original = models.ForeignKey(CriterioAvaliacao, on_delete='CASCADE')
    descricao = models.CharField(max_length=100)
    texto_explicativo = models.TextField(max_length=1000)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete='CASCADE')
    inativo = models.BooleanField()

    def __str__(self):
        return self.descricao[:50] + ...

class OrdemItemAvaliacao(models.Model):
    descricao = models.CharField(max_length=500)
    impacto_nota = models.FloatField()
    nota_maxima = models.ForeignKey(NotaAvaliacao, on_delete='CASCADE')
    criterio_avaliacao = models.ForeignKey(CriterioAvaliacao, on_delete='CASCADE')

    def __str__(self):
        return self.descricao[:50] + '...'

class OrdemGrupoAtividade(models.Model):
    pass

class OrdemAtividade(models.Model):
    pass

class OrdemTipoAtividade(models.Model):
    pass

class Justificativa(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao[:50] + '...'

class Produto(models.Model):
    carga_horaria = models.IntegerField()
    quantidade_produto = models.IntegerField()
    carga_horaria_produto = models.FloatField()
    observacoes = models.CharField(max_length=200)
    observacoes_adicionais = models.CharField(max_length=200)
    motivo = models.CharField(max_length=200)
    avaliacao = models.IntegerField()
    entregue_no_prazo = models.BooleanField()
    data_termino_real = models.DateField()
    grupo_atividade = models.ForeignKey(OrdemGrupoAtividade, on_delete='CASCADE')
    atividade = models.ForeignKey(OrdemAtividade, on_delete='CASCADE')
    tipo_atividade = models.ForeignKey(OrdemTipoAtividade, on_delete='CASCADE')
    pacto = models.ForeignKey(Pacto, on_delete='CASCADE')
    Justificativa = models.ForeignKey(Justificativa, on_delete='CASCADE')

class NivelAvaliacao(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao[:50]

class AvaliacaoProduto(models.Model):
    cpf_avaliador = models.CharField(max_length=11)
    data_avaliacao = models.DateField()
    quantidade_produtos_avaliados = models.IntegerField()
    avaliacao = models.IntegerField()
    entregue_no_prazo = models.BooleanField()
    localizacao_produto = models.CharField(max_length=200, blank=True)
    data_termino_real = models.DateField(blank=True)
    tipo_avaliacao = models.IntegerField()
    nota_final_avaliacao_detalhada = models.FloatField(blank=True)
    justificativa = models.ForeignKey(Justificativa, on_delete='CASCADE')
    produto = models.ForeignKey(Produto, on_delete='CASCADE')
    nivel_avaliacao = models.ForeignKey(NivelAvaliacao, on_delete='CASCADE')

class AvaliacaoDetalhadaProduto(models.Model):
    avaliacao_produto
    ordem_item_avaliacao = models.ForeignKey(OrdemItemAvaliacao, on_delete='CASCADE')
    ordem_criterio_avaliacao = models.ForeignKey(OrdemCriterioAvaliacao, on_delete='CASCADE')






