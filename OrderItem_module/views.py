from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from OrderItem_module.filters import OrderItemFilter
from OrderItem_module.forms import CreateOrderItemModelForm
from OrderItem_module.models import OrderItem
from OrderItem_module.serializers import OrderItemSerializer
from Order_module.models import Order
from Product_module.models import Product
from Product_module.serializers import ProductSerializer
from Order_module.serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from Order_module.filters import OrderFilter
from Product_module.filters import ProductFilter


#Create your views here.



class Create_OrderItem_ModelForm(CreateView):
    form_class = CreateOrderItemModelForm


class OrderItemList(ListView):
    model = OrderItem




class OrderItemUpdateView(UpdateView):
    form_class = CreateOrderItemModelForm
    model = OrderItem



class OrderItemDeleteView(DeleteView):
    model = OrderItem

class OrderItemViewSetApiView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = OrderItemFilter



class ProductViewSetApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = ProductFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]




class OrderViewSetApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = OrderFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]

