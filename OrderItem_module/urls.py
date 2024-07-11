from django.urls import path, include

from OrderItem_module import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.OrderItemViewSetApiView)

router_a = DefaultRouter()
router_a.register('', views.ProductViewSetApiView)

router_b = DefaultRouter()
router_b.register('', views.OrderViewSetApiView)

urlpatterns = [
    path('', views.Create_OrderItem_ModelForm.as_view()),
    path('orderitem-list', views.OrderItemList.as_view()),
    path('<pk>/update', views.OrderItemUpdateView.as_view()),
    path('<pk>/delete', views.OrderItemDeleteView.as_view()),
    path('orderitemviewsets/', include(router.urls)),
    path('productviewsets/', include(router_a.urls)),
    path('orderviewsets/', include(router_b.urls)),
]