from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from Order_module.forms import CreateOrderModelForm
from Order_module.models import Order
from Order_module.serializers import OrderSerializer
from base.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from Order_module.filters import OrderFilter
from base.filters import UserFilter


#Create your views here.



class Create_Order_ModelForm(CreateView):
    form_class = CreateOrderModelForm


class OrderList(ListView):
    model = Order




class OrderUpdateView(UpdateView):
    form_class = CreateOrderModelForm
    model = Order



class OrderDeleteView(DeleteView):
    model = Order

class OrderViewSetApiView(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user').all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = OrderFilter



class UserViewSetApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = UserFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]




