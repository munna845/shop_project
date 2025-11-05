from .models import Category, Product, Order, OrderItem, Cart, CartItem
from .serializers import (
    categoryserializer,
    productserializer,
    orderserializer,
    OrderItemtserializer,
    Cartserializer,
    CartItemserializer
)
from rest_framework import viewsets
from .permissions import IsOwnerOrAdmin



# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoryserializer
    permission_classes = [IsOwnerOrAdmin]


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = productserializer
    permission_classes = [IsOwnerOrAdmin]


# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user').prefetch_related('items__product').all()
    serializer_class = orderserializer
    permission_classes = [IsOwnerOrAdmin]


# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related('product', 'order').all()
    serializer_class = OrderItemtserializer
    permission_classes = [IsOwnerOrAdmin]


# Cart ViewSet
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.select_related('user').prefetch_related('items__product').all()
    serializer_class = Cartserializer
    permission_classes = [IsOwnerOrAdmin]


# CartItem ViewSet
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.select_related('cart', 'product').all()
    serializer_class = CartItemserializer
    permission_classes = [IsOwnerOrAdmin]
