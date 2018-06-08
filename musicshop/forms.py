
from django import forms

from .models import Order,OrderDetail

class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCreationDetail(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'


