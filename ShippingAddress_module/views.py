from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from Order_module.models import Order
from Order_module.serializers import OrderSerializer
from ShippingAddress_module.filters import ShippingAddressFilter
from ShippingAddress_module.forms import ShippingAddressModelForm
from ShippingAddress_module.models import ShippingAddress
from ShippingAddress_module.serializers import ShippingAddressSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from Order_module.filters import OrderFilter


#Create your views here.



class Create_ShippingAddress_ModelForm(CreateView):
    form_class = ShippingAddressModelForm


class ShippingAddressList(ListView):
    model = ShippingAddress




class ShippingAddressUpdateView(UpdateView):
    form_class = ShippingAddressModelForm
    model = ShippingAddress



class ShippingAddressView(DeleteView):
    model = ShippingAddress

class ShippingAddressViewSetApiView(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.select_related('order').all()
    serializer_class = ShippingAddressSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = ShippingAddressFilter



class OrderViewSetApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = OrderFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]




