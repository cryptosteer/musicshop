import datetime

from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from musicshop.models import Articulo, Pedido


def login(request):
    if request.user.is_authenticated and request.user.is_active:
        return redirect("/articulos/")
    else:
        if request.method == 'POST':

            if request.POST.get('username') is None:
                messages.error(request, "Error en usuario y/o contraseña")
            else:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return redirect('/articulos/')
                else:
                    messages.error(request, "Error en usuario y/o contraseña")
                    return redirect('/login/')
        else:
            return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')


def listararticulos(request):
    if request.user.is_authenticated:
        return render(request, 'listaarticulos.html', {'articulos':Articulo.objects.all()})
    else:
        return redirect('/login/')


def crearpedido(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fecha = datetime.datetime.strptime(request.POST.get('fecha'), '%Y-%m-%d')
            pedido = Pedido()
            pedido.fecha = fecha
            pedido.save()
            return redirect('musicshop:listararticulos')
        else:
            return render(request, 'crearpedido.html', {'articulos':Articulo.objects.all()})
    else:
        return redirect('/login/')