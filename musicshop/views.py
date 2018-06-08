from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

#from musicshop.form import

from musicshop.form import crearform
from .models import Article, TipeArticle, Order, DetailOrder


# Create your views here.
def inicio (request):

    return render(request, "musicshop/index.html")


def crear (request):
    form = crearform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('musicshop:listar')
    contexto = {'form': form}
    return render(request, 'musicshop/crear.html', contexto)


def listar (request):
    articles=Article.objects.all()
    data={'articles':articles}
    return render(request,"musicshop/listar.html",context=data)


def editar(request,pk):
    instancia = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = crearform(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('misicshop:listar')
    else:
        form = crearform(instance=instancia)

    contexto = {'form': form}
    return render(request, 'musicshop/editar.html', contexto)