from django.urls import path, include

from ShippingAddress_module import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ShippingAddressViewSetApiView)

router_a = DefaultRouter()
router_a.register('', views.OrderViewSetApiView)

urlpatterns = [
    path('', views.Create_ShippingAddress_ModelForm.as_view()),
    path('ShippingAddress-list', views.ShippingAddressList.as_view()),
    path('<pk>/update', views.ShippingAddressUpdateView.as_view()),
    path('<pk>/delete', views.ShippingAddressView.as_view()),
    path('ShippingAddressviewsets/', include(router.urls)),
    path('Orderviewsets/', include(router_a.urls)),
]