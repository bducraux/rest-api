from django.contrib import admin
from .models import Demanda
from django.utils.html import format_html


class DemandaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'anunciante', 'status']

    def status(self, obj):
        tag = "<img src='/static/img/{}' />"
        if obj.finalizado:
            return format_html(tag.format("ativo.svg"))
        else:
            return format_html(tag.format("finalizado.svg"))

    status.allow_tags = True
    status.short_description = 'Finalizado'


admin.site.register(Demanda, DemandaAdmin)
