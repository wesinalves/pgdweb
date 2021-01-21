from django.db import models
from pdgweb.configurations.models import OrdemServico, TipoPacto

# Create your models here.

class Pacto(models.Model):
    cpf_usuario = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    cpf_dirigente = models.CharField(max_length=200)
    ordem_servico = models.ForeignKey(OrdemServico)
    tipo_pacto = models.ForeignKey(TipoPacto)

class Historico(models.Model):
    descricao = models.CharField(max_length=200)

class Cronograma(models.Model):
    pass




