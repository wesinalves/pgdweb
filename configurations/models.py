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
        return self.faix[:50] + '...'

class GrupoAtividade(models.Model):
    nom_grupo_atividade = models.CharField(max_length=200)
    inativo = models.BooleanField()
    atividades = models.ManyToManyField(Atividade)

    def __str__(self):
        return self.nom_grupo_atividade[:50] + '...'

class TipoPacto(models.Model):
    desc_tipo_pacto = models.CharField(max_length=200)
    unidades = models.ManyToManyField(Unidade, through='Unidade_TipoPacto')

    def __str__(self):
        return self.desc_tipo_pacto[:50] + '...'

class Unidade_TipoPacto(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    tipo_pacto = models.ForeignKey(TipoPacto, on_delete=models.CASCADE)
    pacto_exteriror = models.BooleanField()

class Unidade(models.Model):
    nome = models.CharField(max_length=200)
    sigla =  models.CharField(max_length=20)
    excluido = models.BooleanField()
    codigo = models.CharField(max_length=200)
    unidade_superior = models.OneToOneField(Unidade, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.nome[:50] + '...'

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.IntegerField()
    cpf = models.CharField(max_length=15)
    inativo = models.BooleanField()
    data_nascimento = models.DateTimeField('Data Nascimento')
    unidades = models.ManytoManyField(Unidades, through='UsuarioGrupolUnidade')

    def __str__(self):
        return self.user.username + '...'

class UsuarioGrupolUnidade(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    excluido = models.BooleanField()

