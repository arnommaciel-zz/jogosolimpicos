from django.contrib import admin
from .models import Modalidade, Atleta, Competicao, Resultado

class ModalidadeAdmin(admin.ModelAdmin):
    list_display=('nome','competicao')

class AtletaAdmin(admin.ModelAdmin):
    list_display=('nome_completo','idade')

class CompeticaoAdmin(admin.ModelAdmin):
	list_display=('nome','inicio','fim')

class ResultadoAdmin(admin.ModelAdmin):
	list_filter=('modalidade', 'competicao')
	list_display=('competicao', 'modalidade', 'atleta', 'valor')

admin.site.register(Modalidade, ModalidadeAdmin)
admin.site.register(Atleta, AtletaAdmin)
admin.site.register(Competicao, CompeticaoAdmin)
admin.site.register(Resultado, ResultadoAdmin)
