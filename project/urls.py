from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartProductViewSet, CartViewSet, CustomerViewSet

router = DefaultRouter()
router.register('product', ProductViewSet)
router = DefaultRouter()
router.register('CartProduct', CartProductViewSet)
router = DefaultRouter()
router.register('cart', CartViewSet)
router = DefaultRouter()
router.register('Cusromer', CustomerViewSet)

urlpatterns = router.urls
