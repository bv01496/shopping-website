from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='shop/cat_iamge',blank=True ,default='')
    discounted = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    

class Products(models.Model):
    image = models.ImageField(upload_to='shop/images',blank= False,default="")
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    description = models.TextField()
    discounted = models.BooleanField(default='False')
    tags = models.ManyToManyField(Tags)
    def __str__(self):
        return self.name



class Shopcart(models.Model):
    customer = models.ForeignKey( User,on_delete=models.CASCADE)
    product = models.ForeignKey( Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.customer} has added {self.quantity} number of {self.product} to cart' 

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    location = models.CharField(max_length=250)
    street = models.CharField(max_length=70)
    pincode = models.CharField(max_length=6)
    phonenumber = models.CharField(max_length=12)
    def __str__(self):
        return self.pincode


class Ordered(models.Model):
    customer = models.ForeignKey( User,on_delete=models.CASCADE)
    product = models.ForeignKey( Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    dilivery_address = models.ForeignKey(Address,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.customer} has ordered {self.quantity} number of {self.product}'