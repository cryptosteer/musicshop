from django import forms

from musicshop.models import Order


class crearform(forms.ModelForm):
    class Meta:
        model = Order

        fields =[
            'cliente',
            'vendedor',
            'fecha',
            'total',
        ]

        labels = {
            'Cliente': 'cliente',
            'Vendedor': 'vendedor',
            'Fecha':'fecha',
            'Total': 'total',
        }

        widgets = {
            'cliente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del cliente'}),
            'vendedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del vendedor'}),
            'total': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Total orden'}),
        }





