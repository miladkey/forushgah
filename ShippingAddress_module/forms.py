from django import forms
from ShippingAddress_module.models import ShippingAddress


class ShippingAddressModelForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
       # exclude = ['id']

