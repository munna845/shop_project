from .models import Category, Product, Order, OrderItem, Cart, CartItem
from .serializers import (
    categoryserializer,
    productserializer,
    orderserializer,
    OrderItemtserializer,
    Cartserializer,
    CartItemserializer
)
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrAdmin



# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = categoryserializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_filter = ['name','slug']
    ordering_fields = ['id','name']
    ordering = ['name']


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = productserializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category','price','stock']
    search_fields = ['name','description']
    ordering = ['created_at']


# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user').prefetch_related('items__product').all()
    serializer_class = orderserializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fiels = ['user','paid']
    ordering_fields = ['total','created_at']
    ordering = ['created_at']



# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related('product', 'order').all()
    serializer_class = OrderItemtserializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filters_field = ['order','product']
    ordering_fields = ['quantity','price']
    




# Cart ViewSet
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.select_related('user').prefetch_related('items__product').all()
    serializer_class = Cartserializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filter_fields = ['user']
    ordering=['created_at']


# CartItem ViewSet
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.select_related('cart', 'product').all()
    serializer_class = CartItemserializer
    permission_classes = [IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filter_fields = ['cart','product']
    ordering_fields = ['quantity']
