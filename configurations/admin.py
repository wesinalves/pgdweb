from django.contrib import admin

# Register your models here.
from .models import Atividade, GrupoAtividade, TipoPacto

admin.site.register(Atividade)
admin.site.register(GrupoAtividade)
admin.site.register(TipoPacto)
