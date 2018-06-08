from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from musicshop.forms import UserCreationForm
# Create your views here.

def index(request):
    return render(request, 'index.html')


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


class Logout(LogoutView):
    template_name = 'musicshop/logout.html'

