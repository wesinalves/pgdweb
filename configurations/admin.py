from django.contrib import admin

# Register your models here.
from .models import Atividade, GrupoAtividade, TipoPacto, Usuario, Unidade

admin.site.register(Atividade)
admin.site.register(GrupoAtividade)
admin.site.register(TipoPacto)
admin.site.register(Usuario)
admin.site.register(Unidade)
