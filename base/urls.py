from django.urls import path, include
from base import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', views.UserViewSetApiView)

urlpatterns = [
    path('', views.UserList.as_view()),
    path('creater-user-list', views.CreateUserModelForm.as_view(), name='creater_user_list'),
    path('<pk>/update', views.UserUpdateView.as_view()),
    path('<pk>/delete', views.UserDeleteView.as_view()),
    path('userviewsets/', include(router.urls)),

]