from rest_framework import serializers
from . models import category,product,order,OrderItem,Cart,CartItem
#category serializer
class categoryserializer(serializers.ModelSerializer):
   class Meta:
    model = category
    fields= ['name','slug']

#product serializer
class productserializer(serializers.ModelSerializer):
   class Meta:
    model = product
    fields= ['category','name','slug','description','price','stock','created_at']

#order serializer
class orderserializer(serializers.ModelSerializer):
   class Meta:
    model = order
    fields= ['user','created_at','paid','total']

#OrderItem serializer
class OrderItemtserializer(serializers.ModelSerializer):
   class Meta:
    model = OrderItem
    fields= ['order','product','quantity','price']   

#Cart serializer
class Cartserializer(serializers.ModelSerializer):
   class Meta:
    model = Cart
    fields= ['session_key','created_at']

#CartItem 

class CartItemserializer(serializers.ModelSerializer):
   class Meta:
    model = CartItem
    fields= ['cart','product','quantity']
