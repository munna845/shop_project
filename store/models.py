from django.db import models

# Create your models here.
#category model
class category(models.Model):
 name=models.CharField(max_length=100)
 slug=models.SlugField()

#product model
class product(models.Model):
   category =models.CharField()
   name = models.CharField()
   slug = models.SlugField()
   description = models.TextField()
   price = models.IntegerField()
   stock = models.PositiveIntegerField()
   created_at= models.DateTimeField(auto_now_add=True)
  
#order model
class order(models.Model):
 
     user = models.CharField(max_length=50)
     created_at = models.DateTimeField(auto_now_add=True)
     paid = models.BooleanField(default=False)
     total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
  

# OrderItem model  
class OrderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


#Cart model
class Cart(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)  # session-based cart
    created_at = models.DateTimeField(auto_now_add=True)


#CartItem
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  


 
 
 
 
 

 
 
