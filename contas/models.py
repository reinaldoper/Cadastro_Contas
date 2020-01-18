from django.db import models
from django.db.models import Model, DateTimeField, CharField, TextField, BooleanField, DateField


class Contas(Model):
    data_de_criacao = DateTimeField(auto_now_add=True, verbose_name='data de criação')
    data_de_execucao = DateTimeField(auto_now=True, verbose_name='data de execução')
    tipo_conta = CharField(max_length=200, verbose_name='tipo de conta')
    descricao = TextField(verbose_name='descrição', null=True, blank=True)
    status = BooleanField(default=False, verbose_name='paga')

    class Meta:
        ordering = ['data_de_criacao']

    def __str__(self):
        return self.status
# Create your models here.
