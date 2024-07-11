from django.urls import path, include

from Review_module import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ReviewViewSetApiView)

router_a = DefaultRouter()
router_a.register('', views.ProductViewSetApiView)

router_b = DefaultRouter()
router_b.register('', views.UserViewSetApiView)

urlpatterns = [
    path('', views.Create_Review_ModelForm.as_view()),
    path('review-list', views.ReviewList.as_view()),
    path('<pk>/update', views.ReviewUpdateView.as_view()),
    path('<pk>/delete', views.ReviewDeleteView.as_view()),
    path('reviewviewsets/', include(router.urls)),
    path('productviewsets/', include(router_a.urls)),
    path('userviewsets/', include(router_b.urls)),
]