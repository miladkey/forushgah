from django import forms
from OrderItem_module.models import OrderItem


class CreateOrderItemModelForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
       # exclude = ['id']