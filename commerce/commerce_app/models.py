from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    image=models.ImageField(upload_to="media",null=True,blank=True)
    descriptions=models.TextField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name 

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=False,blank=False)
    vendor=models.CharField(max_length=200,null=False,blank=False)
    product_image=models.ImageField(upload_to='media',null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False) 
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)  
    descriptions=models.TextField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)  




 

