from django.contrib import admin

admin.site.site_header = 'Programa de Gestão de Demandas'
admin.site.index_title = 'Ministério das Comunicações'

# Register your models here.
from .models import Atividade, TipoAtividade, GrupoAtividade, \
    TipoPacto, Usuario, Unidade, Unidade_TipoPacto, UsuarioGrupolUnidade, \
    CriterioAvaliacao, ItemAvaliacao, NotaAvaliacao, OrdemServico

from .forms import TipoAtividadeForm

class ItemAvaliacaoInline(admin.TabularInline):
    model = ItemAvaliacao

class CriterioAvaliacaoAdmin(admin.ModelAdmin):
    inlines = [ItemAvaliacaoInline]

class TipoAtividadeInline(admin.TabularInline):
    model = TipoAtividade
    form = TipoAtividadeForm
    

class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nom_atividade', 'inativo')
    fieldsets = [
        ('Atividade', {'fields': ['nom_atividade']}),
        ('Extra', {'fields': ['inativo','pacto_minimo_reducao', 'descricao_link']}),
    ]
    inlines = [TipoAtividadeInline]

    list_filter = ['pacto_minimo_reducao']

    search_fields = ['nom_atividade']

# admin.site.register(Atividade)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(CriterioAvaliacao, CriterioAvaliacaoAdmin)
admin.site.register(NotaAvaliacao)
admin.site.register(GrupoAtividade)
admin.site.register(TipoPacto)
admin.site.register(Usuario)
admin.site.register(Unidade)
admin.site.register(UsuarioGrupolUnidade)
admin.site.register(Unidade_TipoPacto)
admin.site.register(OrdemServico)