from django.contrib import admin

# Register your models here.
from musicshop.models import Articulo, TipoArticulo, Cliente, Vendedor, Pedido, DetallePedido


@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula',)


@admin.register(Vendedor)
class AdminVendedor(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'sector',)


@admin.register(TipoArticulo)
class AdminTipoArticulo(admin.ModelAdmin):
    list_display = ('tipo',)


@admin.register(Articulo)
class AdminArticulo(admin.ModelAdmin):
    list_display = ('genero', 'artista', 'valor', 'year',)


@admin.register(Pedido)
class AdminPedido(admin.ModelAdmin):
    list_display = ('clientePedido', 'vendedorPedido', 'fecha', 'total',)


@admin.register(DetallePedido)
class AdminDetalleProducto(admin.ModelAdmin):
    list_display = ('articulo', 'cantidad', 'valor')