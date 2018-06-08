from django import forms
from .models import User, Pedido, DetallePedido


class UserCreationForms(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):

        user = super(UserCreationForms, self).save(commit=False)
        if len(User.objects.filter(username=user.username)) == 0:
            user.set_password(self.cleaned_data["password"])
        else:
            if user.password != User.objects.get(username=user.username).password:
                user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'cliente',
            'vendedor',
            'total',
        ]

        labels = {
            'cliente': 'Cliente',
            'vendedor': 'Vendedor',
            'total': 'Total',
        }


class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = [
            'pedido',
            'articulo',
            'cantidad',
            'valor',
        ]

        labels = {
            'pedido': 'Pedido',
            'articulo': 'Articulo',
            'cantidad': 'Cantidad',
            'valor': 'Valor',
        }

