from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from musicshop.models import Articulo


def home(request):
    return render(request, '')


class ArticuloListView(TemplateView):
    template_name = 'articulos/index.html'
    model = Articulo
    context_object_name = 'articulos'
