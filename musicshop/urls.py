from django.conf.urls import url

from musicshop import views
from musicshop.views import crear, inicio, listar

app_name = "musicshop"
urlpatterns = [
    url(r'inicio/$', inicio, name="inicio"),
    url(r'^crear/$', views.crear, name="crear"),
    url(r'^listar/$', views.listar, name="listar"),
    url(r'^editar/(?P<pk>\d+)/$', views.editar, name="editar"),


]
