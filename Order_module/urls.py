from django.urls import path, include

from Order_module import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.OrderViewSetApiView)

_router = DefaultRouter()
_router.register('', views.UserViewSetApiView)

urlpatterns = [
    path('', views.Create_Order_ModelForm.as_view()),
    path('order-list', views.OrderList.as_view()),
    path('<pk>/update', views.OrderUpdateView.as_view()),
    path('<pk>/delete', views.OrderDeleteView.as_view()),
    path('orderviewsets/', include(router.urls)),
    path('userviewsets/', include(_router.urls)),
]