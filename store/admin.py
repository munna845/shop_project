from django.contrib import admin
from . models import category,product,OrderItem,Cart,CartItem
 
# Register your models here.
@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
  list_display=['name','slug']

@admin.register(product)
class productAdmin(admin.ModelAdmin):
  
  list_display= ['category','name','slug','description','price','stock','created_at']

class OrderAdmin(admin.ModelAdmin):
  
  list_display= ['user','created_at','paid','total']  
 


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
  
  list_display= ['order','product','quantity','price']   



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
  
  list_display= ['session_key','created_at']



@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
  
  list_display= ['cart','product','quantity']


