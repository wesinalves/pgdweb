from django.db import models

# Create your models here.
# Create your models here.
class Atividade(models.Model):
    nom_atividade = models.CharField(max_length=200)
    pacto_minimo_reducao = models.IntegerField()
    inativo = models.BooleanField()
    descricao_link = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_atividade[:50] + '...'

class GrupoAtividade(models.Model):
    nom_grupo_atividade = models.CharField(max_length=200)
    inativo = models.BooleanField()

    def __str__(self):
        return self.nom_grupo_atividade[:50] + '...'

class TipoPacto(models.Model):
    desc_tipo_pacto = models.CharField(max_length=200)

    def __str__(self):
        return self.desc_tipo_pacto[:50] + '...'

class Perfil(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome[:50] + '...'

class Unidade(models.Model):
    nome = models.CharField(max_length=200)
    sigla =  models.CharField(max_length=20)
    excluido = models.BooleanField()
    codigo = models.CharField(max_length=200)
    id_unidade_superior = models.IntegerField()

    def __str__(self):
        return self.nome[:50] + '...'

class UsuarioPerfilUnidade(models.Model):
    id_unidade = models.IntegerField()
    id_usuario = models.IntegerField()
    id_perfil = models.IntegerField()
    excluido = models.BooleanField()
