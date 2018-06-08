from django.conf.urls import url
from . import views


app_name='pedidos'
urlpatterns = [
    url(r'^$', views.index, name="index"),

    # CRUD Pedido
    url(r'^pedido/create/$', views.PedidoCreate.as_view(), name="pedido_create"),
    url(r'^pedido/list/$', views.PedidoList.as_view(), name="pedido_list"),
    url(r'^pedido/update/(?P<pk>[0-9]+)/$', views.PedidoUpdate.as_view(), name="pedido_update"),
    url(r'^pedido/delete/(?P<pk>[0-9]+)/$', views.PedidoDelete.as_view(), name="pedido_delete"),
    url(r'^pedido/detail/(?P<pk>[0-9]+)/$', views.PedidoDetail.as_view(), name="pedido_detail"),

    # CRUD Detalle Pedido
    url(r'^pedido/create/$', views.PedidoCreate.as_view(), name="detallepedido_create"),
    url(r'^pedido/list/$', views.PedidoList.as_view(), name="detallepedido_list"),
    url(r'^pedido/update/(?P<pk>[0-9]+)/$', views.PedidoUpdate.as_view(), name="detallepedido_update"),
    url(r'^pedido/delete/(?P<pk>[0-9]+)/$', views.PedidoDelete.as_view(), name="detallepedido_delete"),
    url(r'^pedido/detail/(?P<pk>[0-9]+)/$', views.PedidoDetail.as_view(), name="detallepedido_detail"),
]
