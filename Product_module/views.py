from django.contrib.auth.models import User
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from Product_module.forms import ProductModelForm
from Product_module.models import Product
from Product_module.serializers import ProductSerializer
from base.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from Product_module.filters import ProductFilter
from base.filters import UserFilter


#Create your views here.



class CreateProductModelForm(CreateView):
    form_class = ProductModelForm


class ProductList(ListView):
    model = Product







class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)



class ProductUpdateView(UpdateView):
    form_class = CreateProductModelForm
    model = Product



class ProductDeleteView(DeleteView):
    model = Product

class ProductViewSetApiView(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('user').all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = ProductFilter



class UserViewSetApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = UserFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]




