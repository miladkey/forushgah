from django import forms
from Order_module.models import Order


class CreateOrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
       # exclude = ['id']

