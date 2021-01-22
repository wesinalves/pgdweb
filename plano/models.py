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





