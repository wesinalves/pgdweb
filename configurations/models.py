from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Create your models here.
class Atividade(models.Model):
    nom_atividade = models.CharField(max_length=200)
    pacto_minimo_reducao = models.IntegerField()
    inativo = models.BooleanField()
    descricao_link = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_atividade[:50] + '...'

class TipoAtividade(models.Model):
    faixa = models.CharField(max_length=200)
    texto_explicativo = models.CharField(max_length=300)
    duracao_faixa = models.FloatField()
    duracao_faixa_presencial = models.FloatField()
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    # o nome TipoAtividade deveria ser alterado pois causa confusão nos relacionamentos

    def __str__(self):
        return self.faixa[:50] + '...'

class Unidade(models.Model):
    nome = models.CharField(max_length=200)
    sigla =  models.CharField(max_length=20)
    excluido = models.BooleanField()
    codigo = models.CharField(max_length=200)
    unidade_superior = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nome[:50] + '...'

class TipoPacto(models.Model):
    desc_tipo_pacto = models.CharField(max_length=200)
    unidades = models.ManyToManyField(Unidade, through='Unidade_TipoPacto')

    def __str__(self):
        return self.desc_tipo_pacto[:50] + '...'

        
class GrupoAtividade(models.Model):
    nom_grupo_atividade = models.CharField(max_length=200)
    inativo = models.BooleanField()
    tipo_pactos = models.ManyToManyField(TipoPacto)
    atividades = models.ManyToManyField(Atividade)

    def __str__(self):
        return self.nom_grupo_atividade[:50] + '...'


class Unidade_TipoPacto(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    tipo_pacto = models.ForeignKey(TipoPacto, on_delete=models.CASCADE)
    pacto_exteriror = models.BooleanField()


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField()
    cpf = models.CharField(max_length=15)
    inativo = models.BooleanField()
    data_nascimento = models.DateTimeField('Data Nascimento')
    unidades = models.ManyToManyField(Unidade, through='UsuarioGrupolUnidade')

    def __str__(self):
        return self.user.username + '...'

class UsuarioGrupolUnidade(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    excluido = models.BooleanField()

class CriterioAvaliacao(models.Model):
    descricao = models.CharField(max_length=100)
    texto_explicativo = models.TextField(max_length=1000)
    inativo = models.BooleanField()

    def __str__(self):
        return self.descricao[:50] + '...'

class NotaAvaliacao(models.Model):
    descricao = models.CharField(max_length=20)
    avaliacao_simplificada = models.BooleanField()
    avaliacao_detalhada = models.BooleanField()
    limite_superior = models.FloatField()
    limite_inferior = models.FloatField()
    conceito = models.IntegerField(blank=True)

    def __str__(self):
        return self.descricao[:50] + '...'
        
class ItemAvaliacao(models.Model):
    descricao = models.CharField(max_length=500)
    impacto_nota = models.FloatField()
    nota_maxima = models.ForeignKey(NotaAvaliacao, on_delete=models.CASCADE)
    criterio_avaliacao = models.ForeignKey(CriterioAvaliacao, on_delete=models.CASCADE)
    inativo = models.BooleanField()

    def __str__(self):
        return self.descricao[:50] + '...'

class OrdemServico(models.Model):
    descricao = models.TextField(max_length=1000)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    inativo = models.BooleanField()
    grupo_atividades = models.ManyToManyField(GrupoAtividade)
    criterio_avaliacoes = models.ManyToManyField(CriterioAvaliacao)

    def __str__(self):
        return self.descricao[:50]    

