from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views import View
from django.views.defaults import page_not_found
from django.views.generic import ArchiveIndexView, DeleteView, UpdateView, DetailView
from django.http import Http404

from .forms import FormContas
from .models import Contas


class Home(View):
    template_name = 'contas/home.html'
    context = {}
    context['counter'] = Contas.objects.filter(status=True).count()

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name, self.context, RequestContext(request))


class ContasView(ArchiveIndexView):
    model = Contas
    date_field = 'data_de_criacao'
    template_name = 'contas/conta_archive.html'


class ContasDetail(DetailView):
    model = Contas
    template_name = 'contas/detalhes.html'


class AdicionaConta(View):
    template_name = 'contas/cria_conta.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormContas()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = FormContas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contas/')
        else:
            self.context['form'] = form
            return render_to_response(self.template_name, self.context, RequestContext(request))


class DeleteConta(DeleteView):
    template_name = 'contas/deletar_conta.html'
    model = Contas
    context_object_name = 'contas'
    context = {}

    def get_success_url(self):
        return reverse_lazy('contas:contas')


class AtualizaUpdateView(UpdateView):
    model = Contas
    form_class = FormContas
    template_name = 'contas/atualiza.html'

    def get_success_url(self):
        return reverse_lazy('contas:contas')


def handler404(request, exception, template_name="contas/404.html"):
    response = render_to_response("contas/404.html")
    response.status_code = 404
    return response



# Create your views here.
