from django.urls import path, include

from Product_module import views
from .views import ProductDetailAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProductViewSetApiView)

_router = DefaultRouter()
_router.register('', views.UserViewSetApiView)

urlpatterns = [
    path('', views.CreateProductModelForm.as_view()),
    path('product-list', views.ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail-api'),
    path('<pk>/update', views.ProductUpdateView.as_view()),
    path('<pk>/delete', views.ProductDeleteView.as_view()),
    path('productviewsets/', include(router.urls)),
    path('userviewsets/', include(_router.urls)),
]


