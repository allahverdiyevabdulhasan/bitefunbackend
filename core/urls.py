# core/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, ProductViewSet, OrderViewSet, LikeViewSet, CommentViewSet, NotificationViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API URL'lerini buraya ekliyoruz
]

urlpatterns = [
    # Diğer URL'ler...
    path('api-token-auth/', obtain_auth_token),  # Token almak için
]
