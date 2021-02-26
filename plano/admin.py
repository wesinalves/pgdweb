from django.contrib import admin


# Register your models here.
from .models import OrdemAtividade, OrdemTipoAtividade, OrdemGrupoAtividade, \
    Pacto, Produto, Historico, Cronograma, \
    OrdemCriterioAvaliacao, OrdemItemAvaliacao, SituacaoPacto, \
    AvaliacaoDetalhadaProduto, AvaliacaoProduto, NivelAvaliacao

from configurations.models import Usuario

class ProdutoInline(admin.StackedInline):
    model = Produto
    extra = 1

class PactoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Usuário', {'fields': ['nome','matricula_siape','cpf_usuario', 'unidade_exercicio', \
            'telefone_fixo_servidor','telefone_movel_servidor']}),
        ('Ordem de Serviço', {'fields': ['ordem_servico','executado_no_exterior','processo_sei','possui_carga_horaria', \
            'data_prevista_inicio','data_prevista_termino','carga_horaria','carga_horaria_total']}),
        ('Pacto', {'fields': ['situacao_pacto','motivo','suspensao_inicio', \
            'suspensao_termino','entregue_no_prazo','data_termino_real','data_interrupcao','tipo_pacto','tap']}),
        ('Dirigente', {'fields': ['cpf_solicitante','status_aprovacao_solicitante','cpf_dirigente','status_aprovacao_dirigente', \
            'data_aprovacao_dirigente','cpf_criador','visualizacao_restrita','justificativa_visualizacao_restrita']}),
    ]
    list_filter = ['unidade_exercicio','situacao_pacto', 'tipo_pacto']

    search_fields = ['nome','matricula','cpf_usuario']

    inlines = [
        ProdutoInline,
    ]

    def get_changeform_initial_data(self, request):
        user = request.user
        return {'nome': user.first_name + ' ' + user.last_name,
                'matricula_siape': user.usuario.matricula,
                'cpf_usuario': user.usuario.cpf}
    

        
# Register your models here.
admin.site.register(Pacto, PactoAdmin)
admin.site.register(SituacaoPacto)
admin.site.register(AvaliacaoProduto)
admin.site.register(AvaliacaoDetalhadaProduto)
