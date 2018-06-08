from django.contrib import admin
from django import forms
from django.forms import formset_factory
from .models import Pedido, DetallePedido, User, ClientProfile, Articulo, TipoArticulo, VendedorProfile




class PedidoModelForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'



class DetallePedidoModelForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'


class DetalleInLineTabulard(admin.TabularInline):
    model = DetallePedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    form = PedidoModelForm
    inlines = [DetalleInLineTabulard]


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    form = DetallePedidoModelForm


admin.site.register(User)
admin.site.register(ClientProfile)
admin.site.register(VendedorProfile)
admin.site.register(TipoArticulo)
admin.site.register(Articulo)