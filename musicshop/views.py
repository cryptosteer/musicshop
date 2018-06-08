from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.list import ListView
from django.views import View
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import OrderCreationForm, OrderCreationDetail
from .models import Articule


def index(request):
    return render(request,'user/index.html')

class CreateOrder(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'invoice/invoice.html', {'form': OrderCreationForm()})

    def post(self, request):
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            form.save()

class login(View):

    def get(self, request):
        if request.user.is_authenticated and request.user.is_active:
            return redirect('musicshop:create_order_detail')
        else:
            return  render(request, 'user/login.html')

    def post(self, request):
        if request.POST.get('username') is None:
            messages.error(request, "Error en usuario y/o contraseña")
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('musicshop:create_order')
            else:
                return render(request,'user/login.html')


class CreateOrderDetail(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'invoice/invoice_detail.html', {'form': OrderCreationDetail()})

    def post(self, request):
        form = OrderCreationDetail(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicshop:create_order_detail')



class ArticuleListView(ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    model = Articule
    template_name = 'articules/articules.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



