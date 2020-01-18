from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Contas


class ContasAdmin(ModelAdmin):
    fields = ['tipo_conta','descricao','status']
    list_display = ['tipo_conta', 'descricao', 'data_de_criacao','data_de_execucao', 'status']
    list_editable = ['status']


admin.site.register(Contas, ContasAdmin)

# Register your models here.
