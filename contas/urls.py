from django.template.response import TemplateResponse
from django.urls import path
from django.conf.urls import handler404
from django.conf import settings
from .views import Home, ContasView, ContasDetail, AdicionaConta, DeleteConta, AtualizaUpdateView

app_name = 'contas'
urlpatterns = [
    path('', Home.as_view()),
    path('contas/', ContasView.as_view(), name='contas'),
    path('contas/<int:pk>/', ContasDetail.as_view()),
    path('contas/criar/', AdicionaConta.as_view()),
    path('contas/excluir/<int:pk>/', DeleteConta.as_view()),
    path('contas/atualiza/<int:pk>/', AtualizaUpdateView.as_view()),
]


