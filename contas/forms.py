from django.forms import ModelForm
from .models import Contas


class FormContas(ModelForm):
    class Meta:
        model = Contas
        fields = ['tipo_conta', 'descricao', 'status']