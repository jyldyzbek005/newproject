from rest_framework import serializers
from .models import Product,CartProduct,Cart,Category,Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('category', 'title', 'slug', 'image', 'description', 'price')

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('user', 'cart' ,'product', 'qty', 'final_price')

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('owner', 'products', 'total_products', 'final_price', 'in_order', 'for_anonymous_user')
class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('user', 'phone', 'address')

