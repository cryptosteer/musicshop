from django.contrib import admin

# Register your models here.
from musicshop.models import Perfil, Cliente, Vendedor, Articulo, Pedido, Detalle_p


@admin.register(Perfil)
class Log(admin.ModelAdmin):
    list_display = ('nombre', 'num_tel', 'identificacion',)


@admin.register(Cliente)
class Log(admin.ModelAdmin):
    list_display = ('nombre', 'num_tel', 'identificacion','direccion',)


@admin.register(Vendedor)
class Log(admin.ModelAdmin):
    list_display = ('nombre', 'num_tel', 'identificacion','codigo',)


@admin.register(Articulo)
class Log(admin.ModelAdmin):
    list_display = ('genero', 'album', 'artista', 'ano', 'valor', 'tipo_articulo',)


@admin.register(Pedido)
class Log(admin.ModelAdmin):
    list_display = ('referencia', 'clt', 'vnd', 'fecha') #,

@admin.register(Detalle_p)
class Log(admin.ModelAdmin):
    list_display = ('art', 'cant','r')