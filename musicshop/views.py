from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, CreateView, ListView
from musicshop.forms import UserCreationForm, OrderCreationForm
from musicshop.models import TArticle, Article, Order

# Create your views here.
class ArticleView(ListView):
    model = Article
    template_name = 'order/list.html'

class OrderView(ListView):
    model = Order
    template_name = 'order/list.html'


class TArticleCreateView(CreateView):
    model = TArticle
    fields = '__all__'
    template_name = 'order/register.html'


class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    template_name = 'order/register.html'



class OrderCreateView(FormView):
    form_class = OrderCreationForm
    template_name = 'order/register.html'
    success_url = reverse_lazy('musicshop:dashboard')

    def form_valid(self, form):
        valid = super(OrderCreateView, self).form_valid(form)
        form.save()
        return valid

def index(request):
    if request.user.is_authenticated:
        return redirect('musicshop:dashboard')
    return render(request, 'index.html')



@login_required
def dashboard(request):
    return render(request, 'musicshop/dashboard.html')


class UserRegister(FormView):
    form_class = UserCreationForm
    template_name = 'musicshop/register.html'
    success_url = reverse_lazy('musicshop:login')

    def form_valid(self, form):
        valid = super(UserRegister, self).form_valid(form)
        form.save()
        return valid


class Login(LoginView):
    template_name='musicshop/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'musicshop/logout.html'

