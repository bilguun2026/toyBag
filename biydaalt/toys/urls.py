from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, CategoryViewSet, ToyViewSet, UserViewSet

router = DefaultRouter()
router.register(r'toys', ToyViewSet)
router.register(r'cartItem', CartItemViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
