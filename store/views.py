from . models import category,product,order,OrderItem,Cart,CartItem
  
from . serializers import categoryserializer,productserializer,orderserializer,OrderItemtserializer,Cartserializer,CartItemserializer

from rest_framework import viewsets
from .permissions import IsOwnerOrAdmin

# Create your views here.
#category viewsets
class category_viewsets(viewsets.ModelViewSet):
  queryset = category.objects.all()
  serializer_class = categoryserializer
  permission_classes=  [IsOwnerOrAdmin]

# product viewsets
class product_viewsets(viewsets.ModelViewSet):
  queryset= product.objects.all()
  serializer_class= productserializer
  permission_classes=  [IsOwnerOrAdmin]

# order viewsets
class order_viewsets(viewsets.ModelViewSet):
  queryset= order.objects.all()
  serializer_class= orderserializer
  permission_classes=  [IsOwnerOrAdmin]


# OrderItem viewsets
class product_viewsets(viewsets.ModelViewSet):
  queryset= OrderItem.objects.all()
  serializer_class= orderserializer
  permission_classes=  [IsOwnerOrAdmin]


# Cart viewsets
class Cart_viewsets(viewsets.ModelViewSet):
  queryset= Cart.objects.all()
  serializer_class= Cartserializer
  permission_classes=  [IsOwnerOrAdmin]



# CartItem viewsets
class CartItem_viewsets(viewsets.ModelViewSet):
  queryset= CartItem.objects.all()
  serializer_class= CartItemserializer
  permission_classes=  [IsOwnerOrAdmin]
