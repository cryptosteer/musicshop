from django.contrib import admin

from musicshop.models import Tipoarticulo,Cliente,Vendedor,Articulo,Pedido


class AdminTipoarticulo(admin.ModelAdmin):
    list_display = ['id','tarticulo']

class AdminCliente(admin.ModelAdmin):
    list_display = ['id','nombre', 'cedula','direccion']

class AdminVendedor(admin.ModelAdmin):
    list_display = ['id','nombre', 'cedula','direccion']

class AdminArticulo(admin.ModelAdmin):
    list_display = ['id','genero','tipo_articulo','album','año','valor']

class AdminPedido(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'vendedor', 'articulo', 'fecha', 'cantidad','valor','total']


admin.site.register(Tipoarticulo,AdminTipoarticulo)
admin.site.register(Cliente,AdminCliente)
admin.site.register(Vendedor,AdminVendedor)
admin.site.register(Articulo,AdminArticulo)
admin.site.register(Pedido,AdminPedido)


