from django.contrib import admin

# Register your models here.
from musicshop.models import (
    Articulo,
    Vendedor,
    Cliente,
    Pedido,
    DetallePedido,
)


@admin.register(Articulo)
class AdminArticulo(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'descripcion', 'tipo',)
    exclude = ('slug', )


@admin.register(Vendedor)
class AdminVendedor(admin.ModelAdmin):
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email',)
    exclude = ('slug', )


@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    list_display = ('pk', 'cedula', 'nombre', 'apellido',)
    exclude = ('slug', )


class DetallePedidoStackInline(admin.StackedInline):
    model = DetallePedido
    max_num = 2
    exclude = ('slug', )


@admin.register(Pedido)
class AdminPedido(admin.ModelAdmin):
    list_display = ('pk', 'cliente', 'vendedor', 'fecha', 'total',)
    exclude = ('slug', )
    inlines = (DetallePedidoStackInline,)


@admin.register(DetallePedido)
class AdminDetallePedido(admin.ModelAdmin):
    list_display = ('pk', 'pedido', 'articulo', 'cantidad', 'valor',)
    exclude = ('slug', )

