from django import forms

from musicshop.models import Pedido


class FormularioAddPedido (forms.ModelForm):

    class Meta:
        model=Pedido
        fields= '__all__'
