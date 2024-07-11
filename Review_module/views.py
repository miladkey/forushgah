from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from Product_module.models import Product
from Product_module.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from Product_module.filters import ProductFilter
from Review_module.filters import ReviewFilter
from Review_module.forms import ReviewModelForm
from Review_module.models import Review
from Review_module.serializers import ReviewSerializer
from base.filters import UserFilter
from base.serializers import UserSerializer


#Create your views here.



class Create_Review_ModelForm(CreateView):
    form_class = ReviewModelForm


class ReviewList(ListView):
    model = Review




class ReviewUpdateView(UpdateView):
    form_class = ReviewModelForm
    model = Review



class ReviewDeleteView(DeleteView):
    model = Review

class ReviewViewSetApiView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = ReviewFilter



class ProductViewSetApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = ProductFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]




class UserViewSetApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = '__all__'
    filterset_class = UserFilter
    #authentication_classes = [BaseAuthentication]
  #  permission_classes = [IsAuthenticated]

