from rest_framework.viewsets import ModelViewSet
from .models import Product , CartProduct, Cart,Customer
from .serializers import ProductSerializer, CartProductSerializer, CartSerializers, CustomerSerializers

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer



class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers



