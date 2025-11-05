from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#category model
class category(models.Model):
 name=models.CharField(max_length=100)
 slug=models.SlugField(unique=True,blank=True)
 
 def __str__(self):
     return self.name


#product model
class product(models.Model):
   category =models.ForeignKey(category, on_delete=models.CASCADE, related_name="product")
   name = models.CharField(max_length=50)
   slug = models.SlugField(unique=True)
   description = models.TextField(max_length=500)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   stock = models.PositiveIntegerField()
   created_at= models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
        return self.name
  
#order model
class order(models.Model):
 
     user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="orders")
     created_at = models.DateTimeField(auto_now_add=True)
     paid = models.BooleanField(default=False)
     total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
     
     def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
  

# OrderItem model  
class OrderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"


#Cart model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart of {self.user.username}"


#CartItem
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


 
 
 
 
 

 
 
