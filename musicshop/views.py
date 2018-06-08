from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Pedido, DetallePedido
from .forms import PedidoForm, DetallePedidoForm


# Create your views here.
def index(request):
    return render(request, "musicshop/index.html")


# Vistas Pedido
class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = "musicshop/pedido_create.html"

    success_url = reverse_lazy('pedidos:pedido_list')


class PedidoList(ListView):
    model = Pedido
    template_name = 'musicshop/pedido_list.html'


class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'musicshop/pedido_create.html'
    success_url = reverse_lazy('pedidos:pedido_list')


class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'musicshop/pedido_delete.html'
    success_url = reverse_lazy('pedidos:pedido_list')


class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'musicshop/pedido_detail.html'


# Vistas DetallePedido
class DetallePedidoCreate(CreateView):
    model = DetallePedido
    form_class = PedidoForm
    template_name = "musicshop/detallepedido_create .html"

    success_url = reverse_lazy('pedidos:')


class DetallePedidoList(ListView):
    model = DetallePedido
    template_name = 'musicshop/detallepedido_list .html'


class DetallePedidoUpdate(UpdateView):
    model = DetallePedido
    form_class = PedidoForm
    template_name = 'musicshop/detallepedido_create .html'
    success_url = reverse_lazy('pedidos:detallepedido_list')


class DetallePedidoDelete(DeleteView):
    model = DetallePedido
    template_name = 'musicshop/detallepedido_delete .html'
    success_url = reverse_lazy('pedidos:detallepedido_list')


class DetallePedidoDetail(DetailView):
    model = DetallePedido
    template_name = 'musicshop/detallepedido_detail .html'
