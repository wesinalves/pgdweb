from django.db import models
from configurations.models import OrdemServico, TipoPacto, CriterioAvaliacao, NotaAvaliacao, GrupoAtividade

# Create your models here.

class SituacaoPacto(models.Model):
    descricao = models.CharField(max_length=200)

class Pacto(models.Model):
    cpf_usuario = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    matricula_siape = models.CharField(max_length=100, blank=True, null=True)
    unidade_exercicio = models.IntegerField()
    telefone_fixo_servidor = models.CharField(max_length=100, blank=True, null=True)
    telefone_movel_servidor = models.CharField(max_length=100, blank=True, null=True)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    executado_no_exterior = models.BooleanField()
    processo_sei = models.CharField(max_length=100, blank=True, null=True)
    possui_carga_horaria = models.BooleanField()
    data_prevista_inicio = models.DateField()
    data_prevista_termino = models.DateField()
    carga_horaria = models.FloatField()
    carga_horaria_total = models.FloatField()
    situacao_pacto = models.ForeignKey(SituacaoPacto, on_delete=models.CASCADE)
    motivo = models.TextField(max_length=500, blank=True, null=True)
    suspensao_inicio = models.DateField(blank=True, null=True)
    suspensao_termino = models.DateField(blank=True, null=True)
    entregue_no_prazo = models.BooleanField(blank=True, null=True)
    data_termino_real = models.DateField(blank=True, null=True)
    data_interrupcao = models.DateField(blank=True, null=True)
    tipo_pacto = models.ForeignKey(TipoPacto, on_delete=models.CASCADE)
    tap = models.TextField(max_length=500, blank=True, null=True)
    cpf_solicitante = models.CharField(max_length=100, blank=True, null=True)
    cpf_solicitante = models.CharField(max_length=100, blank=True, null=True)
    status_aprovacao_solicitante = models.IntegerField(blank=True, null=True)
    cpf_dirigente = models.CharField(max_length=200)
    status_aprovacao_dirigente = models.IntegerField(blank=True, null=True)
    data_aprovacao_dirigente = models.DateField(blank=True, null=True)
    cpf_criador = models.CharField(max_length=100, blank=True, null=True)
    visualizacao_restrita = models.BooleanField()
    justificativa_visualizacao_restrita = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.nome[:50] + '...'

class Historico(models.Model):
    descricao = models.CharField(max_length=200)
    pacto = models.ForeignKey(Pacto, on_delete=models.CASCADE)

class Cronograma(models.Model):
    data = models.DateField()
    hora = models.FloatField()
    dia_util = models.BooleanField()
    feriado = models.BooleanField()
    duracao_feriado = models.FloatField()
    suspenso = models.BooleanField()

class OrdemCriterioAvaliacao(models.Model):
    avaliacao_original = models.ForeignKey(CriterioAvaliacao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    texto_explicativo = models.TextField(max_length=1000)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    inativo = models.BooleanField()

    def __str__(self):
        return self.descricao[:50] + ...

class OrdemItemAvaliacao(models.Model):
    descricao = models.CharField(max_length=500)
    impacto_nota = models.FloatField()
    nota_maxima = models.ForeignKey(NotaAvaliacao, on_delete=models.CASCADE)
    criterio_avaliacao = models.ForeignKey(CriterioAvaliacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao[:50] + '...'

class OrdemGrupoAtividade(models.Model):
    nome = models.CharField(max_length=200)
    inativo = models.BooleanField()
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    grupo_atividade_original = models.ForeignKey(GrupoAtividade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome[:50] + '...'

class OrdemAtividade(models.Model):
    nome = models.TextField(max_length=1000)
    pacto_minimo_reducao = models.IntegerField()
    inativo = models.BooleanField()
    descricao_link = models.CharField(max_length=300)
    id_grupo_atividade = models.IntegerField()
    ordem_grupo_atividade = models.ForeignKey(OrdemGrupoAtividade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome[:50]

class OrdemTipoAtividade(models.Model):
    faixa = models.CharField(max_length=100)
    duracao_faixa = models.FloatField()
    duracao_faixa_presencial = models.FloatField()
    id_atividade = models.IntegerField()
    texto_explicativo = models.TextField(max_length=500)
    atividade = models.ForeignKey(OrdemAtividade, on_delete=models.CASCADE)

    def __str__(self):
        return self.faixa[:50]

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
    grupo_atividade = models.ForeignKey(OrdemGrupoAtividade, on_delete=models.CASCADE)
    atividade = models.ForeignKey(OrdemAtividade, on_delete=models.CASCADE)
    tipo_atividade = models.ForeignKey(OrdemTipoAtividade, on_delete=models.CASCADE)
    pacto = models.ForeignKey(Pacto, on_delete=models.CASCADE)
    Justificativa = models.ForeignKey(Justificativa, on_delete=models.CASCADE)

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
    justificativa = models.ForeignKey(Justificativa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nivel_avaliacao = models.ForeignKey(NivelAvaliacao, on_delete=models.CASCADE)

class AvaliacaoDetalhadaProduto(models.Model):
    avaliacao_produto = models.ForeignKey(AvaliacaoProduto, on_delete=models.CASCADE)
    ordem_item_avaliacao = models.ForeignKey(OrdemItemAvaliacao, on_delete=models.CASCADE)
    ordem_criterio_avaliacao = models.ForeignKey(OrdemCriterioAvaliacao, on_delete=models.CASCADE)






