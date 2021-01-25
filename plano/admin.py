from django.contrib import admin


# Register your models here.
from .models import OrdemAtividade, OrdemTipoAtividade, OrdemGrupoAtividade, \
    Pacto, Produto, Historico, Justificativa, Cronograma, \
    OrdemCriterioAvaliacao, OrdemItemAvaliacao

# Register your models here.
admin.site.register(Pacto)
