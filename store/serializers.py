from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Cart, CartItem

#category serializer
class categoryserializer(serializers.ModelSerializer):
   class Meta:
    model = Category
    fields= ['name','slug']

#product serializer
class productserializer(serializers.ModelSerializer):
   class Meta:
    model = Product
    fields= ['category','name','slug','description','price','stock','created_at']

#order serializer
class orderserializer(serializers.ModelSerializer):
   class Meta:
    model = Order
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
