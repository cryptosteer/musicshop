from django.contrib import admin
from .models import User, ClienteProfile, VendedorProfile, Pedido, DetallePedido, TipoArticulo, Articulo
from .forms import UserCreationForms


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserCreationForms
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_cliente',
                    'is_vendedor',)
    list_filter = ('is_cliente', 'is_vendedor')
    fieldsets = [
        ('User information', {
            'fields': ['username',
                       'password',
                       'first_name',
                       'last_name',
                       'email',
                       'is_cliente',
                       'is_vendedor', ]
        }),
    ]


@admin.register(ClienteProfile)
class ClienteProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


@admin.register(VendedorProfile)
class VendedorProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


@admin.register(TipoArticulo)
class TipoArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'tipo', 'album', 'artista', 'only_year', 'valor',)


class DetallePedidoInLine(admin.StackedInline):
    model = DetallePedido
    extra = 3

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'vendedor', 'fecha', 'total',)
    inlines = [DetallePedidoInLine]

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'articulo', 'cantidad', 'valor')
